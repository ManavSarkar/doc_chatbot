from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain.vectorstores.chroma import Chroma
from .embeddings_model import get_embedding_function
from .prompts import get_prompt
def query_rag(query_text: str, model):
    CHROMA_PATH = "chroma_db"
    db = Chroma(
        persist_directory=CHROMA_PATH,
        embedding_function=get_embedding_function(),
    )
    
    results = db.similarity_search_with_score(query_text, k=5)
    
    context_text = "\n\n".join([doc.page_content for doc, _score in results])
    PROMPT_TEMPLATE = get_prompt()
    prompt_template = ChatPromptTemplate(
        [("system", "You are a helpful AI bot."),
        ("human", PROMPT_TEMPLATE),]
    )
    prompt = prompt_template.format(context=context_text, question=query_text)
    
    response = model.invoke(prompt)
    
    sources = [doc.metadata.get("id") for doc, _score in results]
    
    return response, sources