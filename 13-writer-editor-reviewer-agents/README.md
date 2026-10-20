# Writer, Editor and Reviewer Agents

## Overview

The Writer, Editor and Reviewer Agents project demonstrates a multi-agent AI workflow for content creation. Separate AI roles work together to draft content, edit it for clarity, and review the final output.

## Features

- Generate content from a given topic.
- Edit generated content for clarity and readability.
- Review content for quality and relevance.
- Demonstrate collaboration between multiple AI roles.
- Explore sequential AI workflows.

## Technologies Used

- Python
- LangChain
- Groq API
- Large Language Models (LLMs)

## Project Structure

```text
13-writer-editor-reviewer-agents/
├── writer_agent.py
├── README.md
└── requirements.txt
```

## Installation

```bash
pip install -r requirements.txt
```

## Configuration

Configure the Groq API key using the environment variable expected by the application. Never publish API keys or `.env` files.

## Run the Application

```bash
python writer_agent.py
```

## Learning Objectives

- Understand multi-agent AI workflows.
- Learn how to divide tasks between specialized AI roles.
- Practice prompt engineering.
- Explore AI-assisted writing and content review.
