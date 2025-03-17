from langchain.chains import RetrievalQA
from langchain.llms import OpenAI

def retrieve_and_answer(question, vectorstore, openai_api_key):
    """
    Retrieves relevant chunks and generates an answer using OpenAI.
    """
    qa = RetrievalQA.from_chain_type(
        llm=OpenAI(openai_api_key=openai_api_key, temperature=0),
        chain_type="stuff",
        retriever=vectorstore.as_retriever()
    )
    answer = qa.run(question)
    return answer