from langchain.vectorstores.chroma import Chroma
from langchain.vectorstores import FAISS
from langchain_core.documents import Document
from .embeddings_model import get_embedding_function
from .logger import logger
import tempfile

CHROMA_PATH = tempfile.mkdtemp()

def add_to_chroma(chunks: list[Document]):
    db = Chroma(
        persist_directory=CHROMA_PATH,
        embedding_function=get_embedding_function(),
    )
    # delete the existing chroma db
    ids = db.get(include=[])['ids']
    
    if len(ids) > 0:
        db.delete(ids=ids)
    logger.info("Deleted the existing Chroma database")

    # add or update the chunks in the chroma db
    new_chunks = chunks
    new_chunk_ids = [chunk.metadata.get("id") for chunk in new_chunks]
    db.add_documents(new_chunks, ids=new_chunk_ids)
    
    logger.info(f"Added {len(new_chunks)} chunks to the Chroma database")
    
    db.persist()
    
def search_db(query_text: str, k: int = 5):
    db = Chroma(
        persist_directory=CHROMA_PATH,
        embedding_function=get_embedding_function(),
    )
    results = db.similarity_search_with_score(query_text, k=k)
    return results