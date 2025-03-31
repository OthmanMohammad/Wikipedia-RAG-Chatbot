# Wikipedia RAG Chatbot

A Streamlit-based application that leverages Retrieval Augmented Generation (RAG) to provide accurate answers from Wikipedia content.

## Overview

This application allows users to:
- Input text directly or provide a Wikipedia URL
- Process the document to create embeddings and a vector store
- Ask questions about the content and receive AI-generated answers based on the relevant information

## Features

- **Multiple Input Options**: Upload text directly or fetch content from a Wikipedia URL
- **Text Processing**: Automatically splits documents into manageable chunks
- **Vector Embeddings**: Generates embeddings using OpenAI's embedding models
- **FAISS Vector Store**: Creates efficient, searchable vector stores for quick retrieval
- **RAG Implementation**: Retrieves relevant document chunks before generating answers
- **Comprehensive Logging**: Detailed logging for debugging and monitoring

## Architecture

The application follows a modular architecture:

- `app/main.py`: Streamlit interface and main application flow
- `app/rag/`: Contains the RAG implementation components:
  - `document_loader.py`: Fetches content from Wikipedia
  - `text_splitter.py`: Splits documents into chunks
  - `embeddings.py`: Generates embeddings and creates vector stores
  - `retriever.py`: Retrieves relevant information and generates answers
- `utils/`: Helper utilities such as logging

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/wikipedia-rag-chatbot.git
cd wikipedia-rag-chatbot
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the Streamlit app:
```bash
streamlit run app/main.py
```

2. Open your browser and navigate to `http://localhost:8501`

3. Enter your OpenAI API key

4. Choose your input method:
   - Enter text directly
   - Provide a Wikipedia URL

5. Click "Process Document" to generate embeddings

6. Ask questions about the document in the "Ask a Question" section

## Requirements

- Python 3.8+
- OpenAI API key
- Dependencies listed in `requirements.txt`

## Technologies Used

- **Streamlit**: Web interface
- **LangChain**: Framework for building LLM applications
- **OpenAI**: For embeddings and question answering
- **FAISS**: Vector store for efficient similarity search
- **Wikipedia API**: For fetching Wikipedia content

## Notes

This project is still a work in progress. Features and improvements will be added over time.
