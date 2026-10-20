# AI Travel Planner

## Overview

The AI Travel Planner is a Python application that uses Artificial Intelligence to assist users in planning trips. It can generate travel suggestions and itinerary ideas based on the information provided by the user.

## Features

- Generate AI-assisted travel plans.
- Customize travel suggestions using user inputs.
- Explore destination and itinerary recommendations.
- Provide an interactive travel-planning interface.

## Technologies Used

- Python
- Streamlit
- LangChain
- Groq API
- Large Language Models (LLMs)

## Project Structure

```text
12-ai-travel-planner/
├── travel_planner.py
├── README.md
└── requirements.txt
```

## Installation

```bash
pip install -r requirements.txt
```

## Configuration

Configure the Groq API key using the environment variable expected by the application. Keep credentials private and do not commit `.env` files.

## Run the Application

```bash
streamlit run travel_planner.py
```

## Learning Objectives

- Build an AI-powered planning application.
- Integrate language models with Streamlit.
- Practice prompt engineering.
- Explore personalized content generation.
