import os 
from langchain_groq import ChatGroq
from dotenv import load_dotenv


llm = ChatGroq(
    model="openai/gpt-oss-120b",
    groq_api_key = os.getenv("grop_api_key"))

def writer(topic):
    prompt = f"""
You are a creative and professional writer. Write high-quality, engaging text about the topic. Avoid fluff and keep the facts accurate.

Topic: {topic}Topic:{topic} 
"""
    response = llm.invoke(prompt)
    return response.content

def editor(topic):
    prompt = f"""
     You are a professional copyeditor. 
    Review and polish the following topic or text: {topic}.
    - Fix grammar, clarity, and flow.
    - Keep the original meaning intact.
    - If you lack factual data about the topic, state what is missing rather than guessing.
    """
    response = llm.invoke(prompt)
    return response.content


def review_agent(write):
    prompt = f"""
You are a helpful reviewer agent, look for mistakes and correct it, avoid unnecessary details
write: {write}
"""
    response = llm.invoke(prompt)
    return response.content

def multi_agent(topic):
    write = writer(topic)
    print("----Output of 1s agent")
    print(write)


    edited_output = editor(write)
    print("----Output of 2nd agent")
    print(edited_output)



    final_output = review_agent(edited_output)
    print("----Output of 3rnd agent")
    print(final_output)

multi_agent(input("Enter your topic:"))

#writer
#editor
#reviewer