import streamlit as st
import google.generativeai as genai
import json
import random

API_KEY = "AQ.Ab8RN6Kx4CHeUGO2_hHdFMKShxOP7nWeYHNyKiHrb2PpIMIP3Q"

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")

st.set_page_config(page_title="Guess the Mystery", page_icon="🕵️")

st.title("🕵️ Guess the Mystery")
st.write("Can you solve the mystery before all the clues are revealed?")


categories = [
    "Animals",
    "Countries",
    "Famous Landmarks",
    "Movies",
    "Books",
    "Historical Figures",
    "Technology",
    "Planets",
    "Space",
    "Sports",
    "Musical Instruments",
    "Vehicles",
    "Food",
    "Video Games",
    "Marvel",
    "Disney",
    "Science",
    "Mythology"
]


if "answer" not in st.session_state:

    category = random.choice(categories)

    prompt = f"""
Create a guessing game.

Category: {category}

Choose ONE random answer from this category.

Return ONLY valid JSON.

{{
    "answer":"River",
    "category":"Natural Objects",
    "clues":[
        "...",
        "...",
        "...",
        "...",
        "..."
    ]
}}

Rules:

- The answer must ONLY be the object/person/place name.
- DO NOT return the riddle.
- Create ORIGINAL clues.
- Make clues go from hardest to easiest.
- Return ONLY JSON.
"""

    response = model.generate_content(prompt)

    text = response.text.replace("```json", "").replace("```", "").strip()

    game = json.loads(text)

    st.session_state.answer = game["answer"]
    st.session_state.category = game["category"]
    st.session_state.clues = game["clues"]
    st.session_state.current = 1
    st.session_state.finished = False



st.subheader(f"📂 Category: {st.session_state.category}")

st.subheader("🔍 Clues")

for i in range(st.session_state.current):
    st.write(f"• {st.session_state.clues[i]}")



guess = st.text_input(
    "Your Guess",
    disabled=st.session_state.finished
)

if st.button("Submit Guess", disabled=st.session_state.finished):

    judge_prompt = f"""
Correct Answer:
{st.session_state.answer}

Player Guess:
{guess}

If the player's guess is essentially the same answer,
reply ONLY with

YES

or

NO

Accept:
- minor spelling mistakes
- singular/plural
- abbreviations
- common names
"""

    judge = model.generate_content(judge_prompt).text.strip().upper()

    if "YES" in judge:

        st.success("🎉 Correct!")
        st.balloons()
        st.write(f"The answer was **{st.session_state.answer}**")
        st.session_state.finished = True

    else:

        st.error("❌ Wrong guess!")

        if st.session_state.current < len(st.session_state.clues):
            st.session_state.current += 1
        else:
            st.error("Game Over!")
            st.write(f"The answer was **{st.session_state.answer}**")
            st.session_state.finished = True


if st.button("🔄 New Mystery"):

    for key in list(st.session_state.keys()):
        del st.session_state[key]

    st.rerun()