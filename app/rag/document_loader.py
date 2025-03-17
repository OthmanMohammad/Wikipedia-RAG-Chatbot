from langchain_community.document_loaders import WikipediaLoader
from utils.logger import logger


def load_document(wikipedia_url):
    """
    Fetches content from a Wikipedia link.
    """
    try:
        page_title = wikipedia_url.split("/")[-1]
        logger.info(f"Loading Wikipedia page: {page_title}")
        loader = WikipediaLoader(query=page_title, load_max_docs=1)
        docs = loader.load()
        return docs[0].page_content
    except Exception as e:
        logger.error(f"Error loading Wikipedia document: {e}")
        raise Exception("Failed to load Wikipedia document. Please check the URL and try again.")