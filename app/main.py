import streamlit as st
from rag.document_loader import load_document
from rag.text_splitter import split_text
from rag.embeddings import generate_embeddings, create_vectorstore
from rag.retriever import retrieve_and_answer
from utils.logger import logger


st.title("Wikipedia RAG Chatbot")

# Ask for OpenAI API key
openai_api_key = st.text_input("Enter your OpenAI API key:", type="password")
if not openai_api_key:
    st.warning("Please enter your OpenAI API key to proceed.")
    logger.warning("OpenAI API key not provided.")
    st.stop()

# Input for document
st.header("Upload Document")
input_type = st.radio("Choose input type:", ("Text", "Wikipedia Link"))

if input_type == "Text":
    text = st.text_area("Paste your text here:")
else:
    wikipedia_url = st.text_input("Enter a Wikipedia link:")

# Process document
if st.button("Process Document"):
    if input_type == "Text" and text:
        logger.info("Processing text input.")
        document = text
    elif input_type == "Wikipedia Link" and wikipedia_url:
        logger.info(f"Fetching Wikipedia content from URL: {wikipedia_url}")
        document = load_document(wikipedia_url)
    else:
        logger.error("Invalid input provided.")
        st.error("Please provide valid input.")
        st.stop()

    # Split text into chunks
    logger.info("Splitting text into chunks.")
    chunks = split_text(document)

    # Generate embeddings and create vector store
    logger.info("Generating embeddings and creating vector store.")
    embeddings = generate_embeddings(openai_api_key)
    vectorstore = create_vectorstore(chunks, embeddings)

    # Save vectorstore in session state
    st.session_state.vectorstore = vectorstore
    logger.info("Document processed successfully.")
    st.success("Document processed successfully!")

# Question answering
st.header("Ask a Question")
question = st.text_input("Enter your question:")

if st.button("Get Answer"):
    if "vectorstore" not in st.session_state:
        logger.error("No document processed yet.")
        st.error("Please process a document first.")
        st.stop()

    # Retrieve and answer
    logger.info(f"Retrieving answer for question: {question}")
    answer = retrieve_and_answer(question, st.session_state.vectorstore, openai_api_key)
    logger.info(f"Answer generated: {answer}")
    st.write("**Answer:**", answer)