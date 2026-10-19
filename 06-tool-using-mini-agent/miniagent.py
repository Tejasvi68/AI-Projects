import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.tools import tool
from langchain_classic.agents import initialize_agent, AgentType
from datetime import datetime


@tool 
def calculator(expression: str):
    """Useful for solving math problems."""
    return str(eval(expression))

@tool
def current_time(time:str):
    """Useful for giving current date & time"""
    return datetime.now()

llm = ChatGroq(
    groq_api_key = os.getenv("grop_api_key"),
    model_name = "openai/gpt-oss-120b"
)

agent = initialize_agent(
    tools=[calculator,current_time],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION
)

question = input("Ask:")

if question in ('+','*','-','/'):
    response=agent.invoke(calculator)
else:
    response=llm.invoke(question)

#response=agent.invoke("What is current date & time")
print(response.content)


#Langchain LLM helps connect diff diff tools 
#Lang Graph to build workflow using multiple agents  with memory,loops,human approval 
#Lang smith used to debug and (why this api is not calling) to check response quality accross diff questions 


