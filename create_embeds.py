from dotenv import load_dotenv
import os

# Load variables from .env file
load_dotenv()


from langchain_community.document_loaders import PyMuPDFLoader, DirectoryLoader

def load_pdf(file_path):
    return PyMuPDFLoader(file_path).load()



documents = load_pdf("input/gen_ai_langchain_2024.pdf")
from langchain.text_splitter import RecursiveCharacterTextSplitter, SentenceTransformersTokenTextSplitter
def split_documents(documents):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=512,
        chunk_overlap=52,
        length_function=len,
        add_start_index=True,
    )
    
    # Split the documents into chunks
    return text_splitter.split_documents(documents)

chunks = split_documents(documents)

print(f"Number of Documents: {len(documents)} and Number of Chunks: {len(chunks)}")

import time
from langchain_chroma import Chroma
from langchain_nvidia_ai_endpoints import NVIDIAEmbeddings

# Initialize embeddings
embeddings = NVIDIAEmbeddings(model="nvidia/llama-3.2-nv-embedqa-1b-v1")

# Function to process documents in batches
import gc



def process_in_batches(chunks, batch_size=20):
    db = None
    for i in range(0, len(chunks), batch_size):
        batch = chunks[i:i + batch_size]
        try:
            print(f"Processing batch {i // batch_size + 1}...")
            if db is None:
                db = Chroma.from_documents(batch, embeddings, persist_directory="chroma_db")
            else:
                db.add_documents(batch)
            # Wait and clear memory
            time.sleep(5)
            gc.collect()
        except Exception as e:
            print(f"Error processing batch {i // batch_size + 1}: {e}")
    if db:
        db.persist()
    print("Processing complete.")
    return db
