
import os
from fastapi import FastAPI
from pydantic import BaseModel
from langchain_groq import ChatGroq
from dotenv import load_dotenv


app = FastAPI()

llm = ChatGroq(
    model="openai/gpt-oss-120b",
    groq_api_key = os.getenv("grop_api_key"))

class Question(BaseModel):
    question: str

@app.post("/ask")
def ask_llm(data: Question):
    response = llm.invoke(data.question)
    return {"answer": response.content}