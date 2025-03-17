from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
from utils.logger import logger


def retrieve_and_answer(question, vectorstore, openai_api_key):
    """
    Retrieves relevant chunks and generates an answer using OpenAI.
    """
    try:
        logger.info(f"Retrieving answer for question: {question}")
        qa = RetrievalQA.from_chain_type(
            llm=OpenAI(openai_api_key=openai_api_key, temperature=0),
            chain_type="stuff",
            retriever=vectorstore.as_retriever()
        )
        answer = qa.run(question)
        return answer
    except Exception as e:
        logger.error(f"Error retrieving answer: {e}")
        raise Exception("Failed to retrieve answer. Please check your input and try again.")