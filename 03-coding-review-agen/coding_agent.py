import os 
from langchain_groq import ChatGroq
from dotenv import load_dotenv


llm = ChatGroq(
    model="openai/gpt-oss-120b",
    groq_api_key = os.getenv("grop_api_key"))

def coding_agent(task):
    prompt = f"""
You are a helpful coding agent, give accurate code whithout hallucinating
Task:{task} 
"""
    response = llm.invoke(prompt)
    return response.content

def review_agent(coding):
    prompt = f"""
You are a helpful reviewer agent, look for mistakes and correct it, avoid unnecessary details
Coding: {coding}
"""
    response = llm.invoke(prompt)
    return response.content

def multi_agent(task):
    coding = coding_agent(task)
    print("----Output of 1s agent")
    print(coding)

    final_output = review_agent(coding)
    print("----Output of 2nd agent")
    print(final_output)

multi_agent(input("Enter your task:"))

#writer
#editor
#reviewer