import os
from langchain_groq import ChatGroq

def get_model():
    return ChatGroq(model="llama3-8b-8192")
