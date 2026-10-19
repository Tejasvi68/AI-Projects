# AI Email Generator

## Overview

The AI Email Generator is a Python application designed to help users draft professional customer-support emails with the assistance of Artificial Intelligence. It uses a language model to generate email content based on the information supplied by the user.

## Features

- Generate professional email drafts.
- Customize email content based on the provided context.
- Assist with customer-support communication.
- Provide a simple interactive interface.

## Technologies Used

- Python
- Streamlit
- LangChain
- Groq API
- Large Language Models (LLMs)

## Project Structure

```text
05-customer-email-generator/
├── email_generator.py
├── README.md
└── requirements.txt
```

## Installation

```bash
pip install -r requirements.txt
```

## Configuration

Configure the Groq API key using the environment variable expected by the application. Do not publish API keys or `.env` files.

## Run the Application

```bash
streamlit run email_generator.py
```

## Learning Objectives

- Understand AI-assisted email writing.
- Integrate language models into a Streamlit application.
- Practice prompt engineering.
- Explore productivity applications built with AI.

