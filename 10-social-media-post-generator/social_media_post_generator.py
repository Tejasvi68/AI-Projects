#topic
#platform link insta twitter
#target audience
#post length
#langugage
#tone
#with relevant hashtag 
    
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
        "topic",
        "platform",
        "target_audience",
        "post_length",
        "langugage",
        "tone"
        
    ],
    template="""
    You are an expert social media manager and copywriter. 
Write a high-performing social media post based on the following parameters:

- Topic: {topic}
- Platform: {platform}
- Target Audience: {target_audience}
- Post Length: {post_length} (e.g., short, medium, long, or word/character count)
- Language: {language}
- Tone: {tone}

Instructions:
1. Format the post specifically for {platform} (respecting platform conventions like hooks for LinkedIn, punchy lines for Twitter/X, or visual/engaging formatting for Instagram/Facebook).
2. Include a strong opening hook in the first sentence.
3. Include a clear Call to Action (CTA) at the end.
4. Add 3 to 5 relevant, high-reaching hashtags at the very bottom.
5. Do not include meta-commentary, introductory text, or explanations—output only the ready-to-publish post content.

topic:
{topic}
platform:
{platform}
target_audience:
{target_audience}
post_length:
{post_length}
language:
{language}
tone:
{tone}


"""
)

st.title("AI Social-Media Post Generator")




#User Inputs
topic = st.text_input("Enter Topic on which you want post:")
platform = st.selectbox(
    "Enter your preferred platform",
    ['Linkedin', 'Twitter', 'Instagram', 'Facebook']
)
target_audience = st.text_input("Enter target audience:")
post_length = st.text_input("Enter post length:")
language = st.text_input("Enter language:")
tone = st.selectbox(
    "Enter your tone",
    ['Professional', 'Friendly', 'Soft', 'Straigtforward']
)




#Create Final Prompt
final_prompt = prompt.format(
    topic=topic,
    platform=platform,
    target_audience=target_audience,
    post_length=post_length,
    language=language,
    tone=tone
)

#Generated Ai Response 
response = llm.invoke(final_prompt)


if st.button("Generate Post"):
    if not topic or not platform or not post_length or not language or not target_audience or not tone:
        st.error("Please fill above required inputs")
    else:
        st.write(response.content)
        st.balloons()
 
