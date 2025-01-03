# Document Query App

## Overview
The Document Query App is a Streamlit-based application that allows users to upload PDF files, process their content, and query the information using an AI-powered model. The app leverages various tools such as LangChain, ChromaDB, and Groq's Llama3 model to enable efficient document chunking, embedding, and question answering.

Sample Output:
![Screenshot 2025-01-03 195833](https://github.com/user-attachments/assets/6f5b9c9b-ba19-41f1-8d5a-a32e984fda32)

![Screenshot 2025-01-03 195745](https://github.com/user-attachments/assets/af8998bc-3bd5-481f-81c2-477970c278ec)

## Features
- **PDF Upload**: Upload PDF files for processing.
- **Content Processing**: Splits the PDF content into smaller, manageable chunks.
- **Embedding Storage**: Stores embeddings in a Chroma database for efficient querying.
- **AI Query**: Query the document content using a Llama3-based model.
- **PDF Viewer**: Inline viewing of the uploaded PDF for reference.
- **Error Handling**: Provides detailed error messages for unsupported or invalid PDFs.

## Directory Structure
```plaintext
ManavSarkar-doc_chatbot/
├── main.py
├── requirements.txt
├── input/
├── src/
│   ├── __init__.py
│   ├── chroma_helper.py
│   ├── embeddings_model.py
│   ├── llm_model.py
│   ├── load_env.py
│   ├── logger.py
│   ├── process_pdf.py
│   ├── prompts.py
│   └── query_rag.py
└── .devcontainer/
    └── devcontainer.json
```

### Key Files
- **`main.py`**: The main entry point for the Streamlit app.
- **`requirements.txt`**: Lists all the Python dependencies.
- **`src/`**: Contains all the helper modules for embedding, querying, and logging.
- **`devcontainer.json`**: Dev container configuration for streamlined development.

## Installation

### Prerequisites
- Python 3.11 or higher
- Docker (optional, for Dev Containers)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/<username>/ManavSarkar-doc_chatbot.git
   cd ManavSarkar-doc_chatbot
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. (Optional) Use a Dev Container:
   - Open the repository in a Dev Container-enabled environment (e.g., VSCode with Docker).
   - The environment will be set up automatically using the `devcontainer.json` configuration.

## Usage
1. Run the Streamlit app:
   ```bash
   streamlit run main.py
   ```

2. Open the app in your browser (default: http://localhost:8501).

3. Upload a PDF file in the left column and query its content in the provided input field.

4. View the query results and reference the uploaded PDF in the right column.

## Technical Details

### PDF Processing
- **`process_pdf.py`**: Uses `PyMuPDFLoader` to extract text and metadata from PDFs.
- Splits the text into chunks using the `RecursiveCharacterTextSplitter`.

### Embedding and Storage
- **`embeddings_model.py`**: Generates embeddings using the `sentence-transformers/all-mpnet-base-v2` model.
- **`chroma_helper.py`**: Stores and manages embeddings in a Chroma database.

### Querying
- **`query_rag.py`**: Implements a Retrieval-Augmented Generation (RAG) pipeline for document querying.
- Combines context from the Chroma database with a Llama3-based LLM.

### Logging
- **`logger.py`**: Configures logging for monitoring app activity and errors.

### Prompts
- **`prompts.py`**: Defines a standardized prompt template for the LLM.

## Dev Container
- Includes a pre-configured environment with Python dependencies.
- Runs the app automatically on container attach.

## Dependencies
- Key libraries: `Streamlit`, `LangChain`, `ChromaDB`, `SentenceTransformers`, `PyMuPDF`
- See `requirements.txt` for a complete list.

## Contributing
1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature/<feature_name>
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add <feature_name>"
   ```
4. Push to the branch:
   ```bash
   git push origin feature/<feature_name>
   ```
5. Create a Pull Request.

## License
This project is licensed under the MIT License. See `LICENSE` for more details.

## Acknowledgments
- **LangChain** for simplifying LLM integrations.
- **ChromaDB** for efficient embedding storage and retrieval.
- **Streamlit** for an intuitive web interface.

---
Happy Querying! 🎉

