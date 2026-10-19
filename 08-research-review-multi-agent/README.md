# Multi-Agent Research System

## Overview

The Multi-Agent Research System is a Python project that demonstrates how multiple AI agents can collaborate on a task. One agent generates an initial response, while another agent reviews the generated content to improve its quality.

## Features

- Generate research-oriented content using AI.
- Review and refine generated responses.
- Demonstrate collaboration between multiple agents.
- Explore structured LLM workflows.

## Technologies Used

- Python
- LangChain
- Groq API
- Large Language Models (LLMs)

## Project Structure

```text
08-research-review-multi-agent/
├── multisystem.py
├── README.md
└── requirements.txt
```

## Installation

```bash
pip install -r requirements.txt
```

## Configuration

Configure the Groq API key required by the application through an environment variable. Never commit secrets to the repository.

## Run the Application

```bash
python multisystem.py
```

## Learning Objectives

- Understand multi-agent architectures.
- Explore AI-generated content review.
- Learn to structure sequential LLM workflows.
- Practice prompt engineering and agent coordination.
