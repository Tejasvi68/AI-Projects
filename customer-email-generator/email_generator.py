import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
import streamlit as st

load_dotenv()

llm = ChatGroq(
    groq_api_key = os.getenv("grop_api_key"),
    model_name = "openai/gpt-oss-120b",
    temperature = 0.1

)

#Propmt Template 
prompt = PromptTemplate(
    input_variables=[
        "problem",
        "customer",
        "agent"
    ],
    template="""
Act as a professional customer support agent named "[Agent Name]". Write a clear, polite, and helpful email to our customer named "[Customer Name]" regarding the following issue: "[Describe the Problem]". 

Requirements for the email:
1. Warm and professional greeting using the customer's name.
2. A clear acknowledgment and validation of the problem they are experiencing.
3. A direct explanation of how we are solving or investigating this issue.
4. Next steps, an estimated timeline (if applicable), or an easy way for them to reply if they have more questions.
5. A polite closing signed off by "[Agent Name]".
6. Keep the tone empathetic, calm, and solution-focused. Avoid overly robotic or generic phrasing.

problem:
{problem}

customer:
{customer}

agent:
{agent}

"""
)

#User Inputs
problem = st.text_input("Enter match problem your are facing:")
customer = st.text_input("Enter Customer Name:")
agent = st.text_input("Enter Agent Name:")

#Create Final Prompt
final_prompt = prompt.format(
    problem=problem,
    customer=customer,
    agent=agent
)

#Generated Ai Response 
response = llm.invoke(final_prompt)



if st.button("Generate Email"):
    if not problem or not customer or not agent:
        st.error("Please fill above required inputs")
    else:
        st.write(response.content)
         
