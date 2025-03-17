from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from utils.logger import logger


def generate_embeddings(openai_api_key):
    """
    Generates embeddings using OpenAI's embeddings.
    """
    try:
        logger.info("Generating embeddings.")
        embeddings = OpenAIEmbeddings(openai_api_key=openai_api_key)
        return embeddings
    except Exception as e:
        logger.error(f"Error generating embeddings: {e}")
        raise Exception("Failed to generate embeddings. Please check your API key and try again.")

def create_vectorstore(chunks, embeddings):
    """
    Creates a FAISS vector store from text chunks.
    """
    try:
        logger.info("Creating vector store.")
        vectorstore = FAISS.from_texts(chunks, embeddings)
        return vectorstore
    except Exception as e:
        logger.error(f"Error creating vector store: {e}")
        raise Exception("Failed to create vector store. Please check your input and try again.")