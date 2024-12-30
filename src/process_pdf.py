from langchain_community.document_loaders import PyMuPDFLoader, DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from .logger import logger

def load_pdf(file_path):
    logger.info(f"Loading PDF: {file_path}")
    documents = PyMuPDFLoader(file_path).load()
    # check if the document is empty
    if len(documents) == 0:
        logger.error("No text found in the PDF")
    logger.info(f"Number of Documents: {len(documents)}")
    
    return documents

def split_documents(documents):
    logger.info("Splitting Documents")
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=80,
        length_function=len,
        is_separator_regex=False,
        add_start_index=True,
    )
    
    # Split the documents into chunks
    if not documents:
        logger.error("No documents found")
        return []
    chunks =  text_splitter.split_documents(documents)
    for chunk in chunks:
        source = chunk.metadata.get("source")
        page = chunk.metadata.get("page")
        start_index = chunk.metadata.get("start_index")
        chunk.metadata["id"] = f"{source}_{page}_{start_index}"
    logger.info(f"Number of Documents: {len(documents)} and Number of Chunks: {len(chunks)}")
    
    return chunks