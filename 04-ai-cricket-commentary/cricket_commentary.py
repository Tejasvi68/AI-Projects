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
        "match_situations",
        "batsman",
        "bowler"
    ],
    template="""
You are legendary cricket commentator.
Generate exciting cricket commentary in the style of Ravi Shastri.
Match Situation:
{match_situation}

Batsman on Strike:
{batsman}

Bowler  Name:
{bowler}

Requirements:
-Keep it natural and similar to ravi shastri
"""
)

st.title("AI Cricket Commmentary")

#User Inputs
match_situation = st.text_input("Enter match situation:")
batsman = st.text_input("Enter Batsman Name:")
bowler = st.text_input("Enter Bowler Name:")

#Create Final Prompt
final_prompt = prompt.format(
    match_situation=match_situation,
    batsman=batsman,
    bowler=bowler
)


#Generated Ai Response 
response = llm.invoke(final_prompt)

 
if st.button("Generate Commentary"):
    if not match_situation or not batsman or not bowler:
        st.error("Please fill above required inputs")
    else:
        st.write(response.content)
        st.balloons()
 
