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
        "destination",
        "total_days",
        "budget",
        "total_guests",
        "month",
        "accommodation_type"
        
    ],
    template="""
You are an expert, highly knowledgeable AI Travel Planner. Your goal is to create a comprehensive, tailored, and budget-conscious travel itinerary based on the user's specific inputs.

### User Inputs:
- **Destination:** {destination}
- **Trip Duration:** {total_days} days
- **Total Budget:** {budget} (Include currency indian rupees)
- **Total Guests:** {total_guests} person(s)
- **Month of Travel:** {month}
- **Preferred Accommodation Type:** {accommodation_type}

Please structure your response using the following clear sections:

---

### 1. Trip Overview & Vibe
Provide a brief introduction to {destination} specifically tailored for a trip in {month}. Mention what to expect regarding weather, packing essentials, and the overall vibe of the destination during this time of year.

### 2. Day-by-Day Itinerary
Create a logical, highly optimized day-by-day itinerary for {total_days} days. 
- Group activities by geographical proximity to minimize transit time.
- Include morning, afternoon, and evening slots for each day.
- Specify the type of transport best suited for each day's route.

### 3. Foodie Guide (Famous Spots & Local Cuisine)
Suggest the best places to eat, categorized by:
- **Must-Try Famous Local Dishes:** The traditional food the destination is known for.
- **Iconic Food Spots/Restaurants:** Specific, highly-rated establishments that fit a budget of {budget} for {total_guests} guests.
- **Street Food or Hidden Gems:** Casual or local markets worth exploring.

### 4. Estimated Expense Breakdown
Provide a realistic financial estimation tailored for a total budget of {budget} and {total_guests} guests. Format this as a breakdown or clear list covering:
- **Accommodation:** Estimated cost for {total_days} days staying in a {accommodation_type}.
- **Food & Dining:** Estimated cost per person / total.
- **Activities & Attractions:** Entrance fees and tour estimates.
- **Local Transportation:** Public transit, cabs, or car rental costs.
- *Ensure the total roughly aligns with the provided budget constraint.*

### 5.Bonus Recommendations
- **Nearby Day Trips / Destinations:** 1 to 2 incredible places nearby (within a 1-2 hour radius) that are worth visiting if time permits.
- **Local Travel Tips:** Hidden hacks, safety tips, best transit passes to buy, or cultural etiquette to keep in mind.

Keep the response highly structured, engaging, scannable, and packed with practical value. Avoid vague suggestions; provide real names of places, streets, and landmarks.


destination:
{destination}
total_days:
{total_days}
budget:
{budget}
total_guests:
{total_guests}
month:
{month}
accommodation_type:
{accommodation_type}


"""
)

st.title("AI Travel Planner")

st.image("./travel-planning.webp")


#User Inputs
destination = st.text_input("Enter Destination:")
total_days = st.text_input("Enter Total number of days:")
budget = st.slider("Enter your budget:", min_value=5000, max_value=1000000,step=1000)
total_guests = st.text_input("Enter total number of guests:")
month = st.text_input("Enter in which month you are planning to travel:")
accommodation_type = st.selectbox(
    "Enter your preferred accommodation type",
    ['Hotel', 'Hostel', 'Resort', 'Airbnb / Vacation Rental', 'Homestay']
)



#Create Final Prompt
final_prompt = prompt.format(
    destination=destination,
    total_days=total_days,
    budget=budget,
    total_guests=total_guests,
    month=month,
    accommodation_type=accommodation_type
)

#Generated Ai Response 
response = llm.invoke(final_prompt)


if st.button("Generate Plan"):
    if not destination or not total_days or not budget or not total_guests or not month or not accommodation_type:
        st.error("Please fill above required inputs")
    else:
        st.write(response.content)
        st.balloons()
 
