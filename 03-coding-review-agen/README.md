# AI Coding Review Agent

## Overview

The AI Coding Review Agent is a Python-based application that uses Large Language Models (LLMs) to assist with code generation and review. It follows a multi-step workflow in which an AI agent generates code and another agent reviews the generated output.

## Features

- Generate code based on user requirements.
- Review generated code using an AI model.
- Identify potential errors and areas for improvement.
- Improve code readability and structure.
- Automate basic code review tasks.

## Technologies Used

- Python
- LangChain
- Groq API
- Large Language Models (LLMs)

## Project Structure

```text
03-coding-review-agent/
├── coding_agent.py
├── README.md
└── requirements.txt
```

## Installation

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Configuration

Configure your Groq API key using an environment variable required by the application. Never upload API keys or `.env` files to GitHub.

## Run the Application

```bash
python coding_agent.py
```

## Learning Objectives

- Understand LLM-based code generation.
- Learn AI-assisted code review.
- Explore prompt engineering and agent workflows.
- Integrate language models into Python applications.

