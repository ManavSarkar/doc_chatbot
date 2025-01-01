import streamlit as st
from src.process_pdf import load_pdf, split_documents
from src.embeddings_model import get_embedding_function
from src.chroma_helper import add_to_chroma
from src.query_rag import query_rag
from src.llm_model import get_model
from src.logger import logger
import tempfile
import base64
from streamlit_pdf_viewer import pdf_viewer

# if os is linux
import os
if os.name == 'posix':
    __import__('pysqlite3')
    import sys
    sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')
# Initialize model
model = get_model()
# JavaScript renderer for pdf.js

# Streamlit app
def main():
    st.title("Document Query App")

    if "pdf_processed" not in st.session_state:
        st.session_state["pdf_processed"] = ""
    if "chunks" not in st.session_state:
        st.session_state["chunks"] = None
    
    # Create two columns
    left_col, right_col = st.columns([0.3, 0.7], gap="large")  # Adjust the ratio as needed
    
    with left_col:
        uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])
        if uploaded_file and st.session_state["pdf_processed"] != uploaded_file.file_id:
            st.session_state["pdf_content"] = uploaded_file.read()
            logger.info(f"Uploaded file: {uploaded_file.file_id}")
            with st.spinner("Processing the PDF..."):
                # Load and split the document
                with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
                    temp_file.write(st.session_state["pdf_content"])
                    temp_file_path = temp_file.name

                documents = load_pdf(temp_file_path)
                st.session_state["chunks"] = split_documents(documents)
                try: 
                    # if chunks is empty, show error message and return
                    if len(st.session_state["chunks"]) == 0:
                        logger.error("No text found in the PDF. Please upload a different file.")
                        st.error("No text found in the PDF. Please upload a different file.")
                        return

                    # Add to Chroma database
                    add_to_chroma(st.session_state["chunks"])
                    st.session_state["pdf_processed"] = uploaded_file.file_id
                
                except Exception as e:
                    logger.error(f"Error processing PDF: {e}")
                    st.error("Error processing the PDF. Please try again.")
                    return
                
                finally:
                    # Ensure the temporary file is deleted
                    try:
                        import os
                        os.remove(temp_file_path)
                    except Exception as e:
                        logger.error(f"Error deleting the temporary file: {e}")
            
            st.success("PDF processed and added to the database!")
        
        if uploaded_file:
            # Step 2: Query the document
            query_text = st.text_input("Enter your query")

            if query_text:
                with st.spinner("Searching the database and generating response..."):
                    response, sources = query_rag(query_text, model)

                st.subheader("Response")
                st.write(response.content)

                st.subheader("Sources")
                logger.info(f"Sources: {sources}")
                for source in sources:
                    logger.info(f"Source: {source}")
                    st.write(source)

    with right_col:
        if uploaded_file:

            pdf_viewer(st.session_state["pdf_content"], height=700, width=1000)
            st.toast("PDF file uploaded successfully!")


if __name__ == "__main__":
    st.set_page_config(layout="wide", page_title="Document Query App", page_icon="📄")
    
    
    main()
