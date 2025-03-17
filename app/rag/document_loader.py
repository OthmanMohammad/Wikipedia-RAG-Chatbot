from langchain_community.document_loaders import WikipediaLoader

def load_document(wikipedia_url):
    """
    Fetches content from a Wikipedia link.
    """
    page_title = wikipedia_url.split("/")[-1]
    loader = WikipediaLoader(query=page_title, load_max_docs=1)
    docs = loader.load()
    return docs[0].page_content