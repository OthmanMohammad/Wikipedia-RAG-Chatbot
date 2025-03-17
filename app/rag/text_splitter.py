from langchain.text_splitter import CharacterTextSplitter


def split_text(text):
    """
    Splits text into chunks of 1000 characters with 200 characters overlap.
    """
    text_splitter = CharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        separator="\n"
    )
    chunks = text_splitter.split_text(text)
    return chunks