# Personal Knowledge RAG System

## Overview
A Retrieval-Augmented Generation (RAG) system that answers questions about professional information using a personal CV and GitHub project README files.

## Features
- Loads PDF and Markdown documents.
- Splits documents into chunks.
- Generates embeddings using `sentence-transformers/all-MiniLM-L6-v2`.
- Stores and retrieves information using FAISS.
- Generates context-based answers using an LLM through OpenRouter.
- Provides source citations for retrieved information.

## Tech Stack
- Python
- LangChain
- Hugging Face
- FAISS
- OpenRouter

## How to Run
1. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Configure your OpenRouter API key in the `.env` file.
3. Build and save the vector database.
4. Run the RAG application.

## Note
The system uses retrieved document context to answer questions and provide source references.
