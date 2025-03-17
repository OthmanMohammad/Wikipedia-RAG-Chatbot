from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

def generate_embeddings(openai_api_key):
    """
    Generates embeddings using OpenAI's embeddings.
    """
    embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
    return embeddings

def create_vectorstore(chunks, embeddings):
    """
    Creates a FAISS vector store from text chunks.
    """
    vectorstore = FAISS.from_texts(chunks, embeddings)
    return vectorstore