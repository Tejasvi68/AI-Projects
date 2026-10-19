# FastAPI LLM API

## Overview

FastAPI LLM API is a Python-based application that provides an API interface for interacting with a Large Language Model (LLM).

The application uses FastAPI to accept user questions and generate AI-powered responses using the Groq API and LangChain.

It provides an endpoint that allows clients to submit questions and receive responses in JSON format.

## Features

- Accept user questions through an API endpoint.
- Generate AI-powered responses using an LLM.
- Return responses in JSON format.
- Provide automatic interactive API documentation.
- Support API testing through Swagger UI.

## Technologies Used

- Python
- FastAPI
- Uvicorn
- LangChain
- Groq API

## Project Structure

```text
02-fastapi-llm-api/
├── api_llm.py
├── README.md
└── requirements.txt
```

## Installation

**1. Clone the repository**

```bash
git clone https://github.com/Tejasvi68/AI-Projects.git
```

**2. Navigate to the project folder**

```bash
cd AI-Projects/02-fastapi-llm-api
```

**3. Install the required dependencies**

```bash
pip install -r requirements.txt
```

## Environment Configuration

This project requires a Groq API key to access the language model.

Set your API key using an environment variable. Check `api_llm.py` for the exact variable name expected by the application.

Never upload your API key or `.env` file to GitHub.

## Run the Application

Start the FastAPI development server using:

```bash
uvicorn api_llm:app --reload
```

Once the server starts, open the following URLs in your browser.

**API endpoint:**

```text
http://127.0.0.1:8000
```

**Interactive API documentation:**

```text
http://127.0.0.1:8000/docs
```

**Alternative API documentation:**

```text
http://127.0.0.1:8000/redoc
```

The available endpoints depend on the routes defined in `api_llm.py`.

## Learning Objectives

- Understand how to create REST APIs using FastAPI.
- Integrate Large Language Models into Python applications.
- Process API requests and return JSON responses.
- Learn how to test API endpoints using Swagger UI.

## Future Improvements

- Add request validation and improved error handling.
- Implement authentication and rate limiting.
- Add conversation history.
- Integrate additional language models.
- Deploy the API to a cloud platform.



---

This project is part of my AI Projects collection, which explores Python, Artificial Intelligence, Large Language Models, and AI application development.
