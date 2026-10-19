import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
import streamlit as st

load_dotenv()

llm = ChatGroq(
    groq_api_key = os.getenv("grop_api_key"),
    model_name = "openai/gpt-oss-120b",

)

#Propmt Template 
prompt = PromptTemplate(
    input_variables=[
        "movie_name",
        "actor",
        "style"
    ],
    template="""
Act as a movie dialogue expert and cinematic historian. I will provide you with an actor's name, a movie title, and a specific performance style. 

Your task is to generate 5 of the most famous and iconic dialogues from that specific movie, delivered by that character. 

Please follow these rules strictly:
1. Provide exactly 5 dialogues using a bulleted list.
2. Present the lines in their original style, tone, and emotional delivery (include brief parenthetical stage directions or tone markers if it helps capture the delivery).
3. Do not paraphrase; keep the wording as close to the original screenplay/delivery as possible.
4. Keep the list punchy and scannable without long introductory or concluding text.

Movie_name:
{movie_name}

Actor:
{actor}

Style:
{style}


"""
)

st.title("AI Movie Dialog Generator")
#User Inputs
movie_name = st.text_input("Enter movie name:")
actor = st.text_input("Enter Actor Name:")
style = st.text_input("Enter Style:")

#Create Final Prompt
final_prompt = prompt.format(
    movie_name=movie_name,
    actor=actor,
    style=style
)

#Generated Ai Response 
response = llm.invoke(final_prompt)


if st.button("Generate Dialog"):
    if not movie_name or not actor or not style:
        st.error("Please fill above required inputs")
    else:
        st.write(response.content)
        st.balloons()
 
