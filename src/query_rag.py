from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain.vectorstores.chroma import Chroma
from .embeddings_model import get_embedding_function
from .prompts import get_prompt
from .chroma_helper import search_db
def query_rag(query_text: str, model):
    
    results = search_db(query_text)
    
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