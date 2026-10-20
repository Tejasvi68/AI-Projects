# PDF Question Answering Application

## Overview

The PDF Question Answering Application is an AI-powered application that allows users to upload PDF documents and ask questions about their content.

It uses Streamlit to provide an interactive user interface and FastAPI to handle backend requests. The application extracts text from PDF documents and uses a Large Language Model (LLM) through LangChain and the Groq API to generate answers.

## Features

- Upload PDF documents through a Streamlit interface.
- Enter questions about uploaded documents.
- Extract text from PDF files.
- Generate answers using an LLM.
- Return responses through a FastAPI endpoint.
- Display AI-generated answers in the user interface.
- Provide interactive API documentation through Swagger UI.

## Technologies Used

- Python
- Streamlit
- FastAPI
- LangChain
- Groq API
- PyPDF2
- Requests
- python-dotenv

## Project Structure

```text
14-pdf-qa-llm-app/
├── app.py
├── main.py
├── README.md
└── requirements.txt
```

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Tejasvi68/AI-Projects.git
```

### 2. Navigate to the Project Folder

```bash
cd AI-Projects/14-pdf-qa-llm-app
```

### 3. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

## Environment Configuration

Create a `.env` file in the project folder and add your Groq API key:

```env
grop_api_key=YOUR_GROQ_API_KEY
```


## Running the Application

### Step 1: Start the FastAPI Backend

Open a terminal in the project directory and run:

```bash
uvicorn main:app --reload --port 8000
```

The backend will be available at:

```text
http://127.0.0.1:8000
```

Interactive API documentation:

```text
http://127.0.0.1:8000/docs
```

### Step 2: Start the Streamlit Frontend

Open a second terminal in the same project directory and run:

```bash
streamlit run app.py
```

Streamlit will display a local URL in the terminal. Open that URL in your browser to use the application.

## Application Workflow

1. The user uploads a PDF through the Streamlit interface.
2. The user enters a question about the document.
3. Streamlit sends the PDF and question to the FastAPI backend.
4. FastAPI extracts the text from the PDF.
5. The extracted content and question are sent to the Groq language model.
6. The backend returns the generated answer.
7. Streamlit displays the answer to the user.

## Learning Objectives

- Build interactive applications using Streamlit.
- Develop backend APIs using FastAPI.
- Integrate LLMs with Python applications.
- Process uploaded PDF documents.
- Send HTTP requests between frontend and backend.
- Manage API credentials using environment variables.

## Future Improvements

- Add PDF file-size and file-type validation.
- Improve error handling.
- Support larger documents using text splitting and retrieval.
- Add conversation history.
- Deploy the frontend and backend.
- Add automated tests.



---

Part of the AI-Projects repository, exploring Python, Artificial Intelligence, Large Language Models, and AI application development.
