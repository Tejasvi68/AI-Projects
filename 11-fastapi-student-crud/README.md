# FastAPI Student CRUD API

## Overview

The FastAPI Student CRUD API is a Python project demonstrating how to build REST API endpoints for student-related data. It introduces basic Create, Read, Update, and Delete (CRUD) operations using FastAPI.

## Features

- Create student records.
- Retrieve student information.
- Update existing records.
- Delete student records.
- Explore API endpoints using interactive documentation.

## Technologies Used

- Python
- FastAPI
- Uvicorn
- Pydantic

## Project Structure

```text
11-fastapi-student-crud/
├── test.py
├── README.md
└── requirements.txt
```

## Installation

```bash
pip install -r requirements.txt
```

## Run the Application

If the FastAPI application instance in `test.py` is named `app`, run:

```bash
uvicorn test:app --reload
```

Open the interactive API documentation at:

```text
http://127.0.0.1:8000/docs
```

## Data Storage

If the application uses an in-memory data structure, records will not persist after the server restarts. Database integration can be added as a future improvement.

## Learning Objectives

- Understand REST API development.
- Learn CRUD operations.
- Practice request validation with Pydantic.
- Test API endpoints using Swagger UI.

