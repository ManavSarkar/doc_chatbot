from langchain.vectorstores.chroma import Chroma
from langchain_core.documents import Document
CHROMA_PATH = "chroma_db"
def add_to_chroma(chunks: list[Document]):
    db = Chroma(
        persist_directory=CHROMA_PATH,
        embedding_function=get_embedding_function(),
    )

    # add or update the chunks in the chroma db
    existing_items = db.get()
    if existing_items is None:
        existing_items = {"id": []}
    existing_ids = set(existing_items["ids"])

    print(f"Number of existing items: {len(existing_ids)}")

    new_chunks = [chunk for chunk in chunks if chunk.metadata["id"] not in existing_ids]
    new_chunk_ids = [chunk.metadata["id"] for chunk in new_chunks]
    if not new_chunks:
        print("No new chunks to add")
        return
    db.add_documents(new_chunks, ids=new_chunk_ids)
    db.persist()