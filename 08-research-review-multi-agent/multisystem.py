import os 
from langchain_groq import ChatGroq
from dotenv import load_dotenv

llm = ChatGroq(
    model="openai/gpt-oss-120b",
    groq_api_key = os.getenv("grop_api_key"))

def research_agent(topic):
    prompt = f"""
You are a helpful research agent, summarize your research in less than 500 words
Include real time examples
Topic:{topic} 
"""
    response = llm.invoke(prompt)
    return response.content

def review_agent(research):
    prompt = f"""
You are a helpful reviewer agent, look for mistakes and correct it, avoid unnecessary details
Research: {research}
"""
    response = llm.invoke(prompt)
    return response.content

def multi_agent(topic):
    research = research_agent(topic)
    print("----Output of 1s agent")
    print(research)

    final_output = review_agent(research)
    print("----Output of 2nd agent")
    print(final_output)

multi_agent(input("Enter your topic:")) 


  