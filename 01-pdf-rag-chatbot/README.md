# PDF RAG Chatbot

## Overview

This project demonstrates a Retrieval-Augmented Generation (RAG) application that allows users to ask questions about PDF documents.

The application combines document processing, text embeddings, vector search, and a language model to generate answers based on document content.

## Technologies Used

- Python
- Streamlit
- LangChain
- FAISS
- PyPDF2
- Groq API

## Features

- Upload PDF documents.
- Extract and process document text.
- Split text into smaller chunks.
- Store and retrieve document embeddings.
- Ask questions about document content.
- Generate answers using a language model.

## Installation

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Configuration

Configure your Groq API key using an environment variable if the application requires it.

Never upload your API key or `.env` file to GitHub.

## Run the Application

```bash
streamlit run app.py
```

## Project Structure

```text
01-pdf-rag-chatbot/
├── app.py
├── README.md
└── requirements.txt
```

## Purpose

This project explores PDF processing, semantic search, embeddings, and Retrieval-Augmented Generation using Python.
