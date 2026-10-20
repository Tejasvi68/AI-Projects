import streamlit as st
import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from PyPDF2 import PdfReader

load_dotenv()

st.title("My LLM Apllication")

file = st.file_uploader("Upload yuor document",type="PDF")
if file:
    text = "".join(page.extract_text() for page in PdfReader(file).pages)


    question = st.text_input("Ask me anything")
    if question:
        llm = ChatGroq(
            model="openai/gpt-oss-120b",
            groq_api_key=os.getenv("grop_api_key")
        )

        prompt=f"""
        You are a friendly RAG AI Assistant. Whenver user ask a question
        Always give me output in bullet points.
        Your Document:
        {text}

        Your question:
        {question}
        If you do not find answer in the PDF, just say 'The content is not present'. 
        """

        st.write(llm.invoke(prompt).content)

#llama-3.3-70b-versatile




# pip install -r requirements.txt 








