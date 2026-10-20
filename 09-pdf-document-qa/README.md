# PDF Document Q&A

## Overview

PDF Document Q&A is a Python application that allows users to upload a PDF document and ask questions about its contents. The application extracts document text and uses a language model to generate answers based on the supplied information.

## Features

- Upload PDF documents.
- Extract text from PDFs.
- Submit questions about document content.
- Generate AI-powered answers.
- Interact with documents through a simple interface.

## Technologies Used

- Python
- Streamlit
- PyPDF2
- Groq API
- Large Language Models (LLMs)

## Project Structure

```text
09-pdf-document-qa/
├── newapp.py
├── README.md
└── requirements.txt
```

## Installation

```bash
pip install -r requirements.txt
```

## Configuration

Configure the API key required by the application using an environment variable. Never upload API keys or `.env` files to GitHub.

## Run the Application

```bash
streamlit run newapp.py
```

## Learning Objectives

- Learn PDF text extraction.
- Understand how to send document context to an LLM.
- Build interactive AI applications using Streamlit.
- Explore document-based question answering.
