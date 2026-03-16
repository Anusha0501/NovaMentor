import streamlit as st
import random

from nova_client import ask_nova
from questions import questions
from prompts import evaluate_answer

st.set_page_config(page_title="NovaMentor AI", layout="centered")

st.title("🤖 NovaMentor AI – Interview Coach")

st.write("Practice technical interviews and get AI feedback powered by Amazon Nova.")

# Session state for question
if "question" not in st.session_state:
    st.session_state.question = random.choice(questions)

# Display question
st.subheader("Interview Question")
st.write(st.session_state.question)

# User answer input
answer = st.text_area("Type your answer")

# Evaluate answer
if st.button("Evaluate Answer"):

    if answer.strip() == "":
        st.warning("Please enter an answer.")
    else:

        with st.spinner("Analyzing answer using Amazon Nova..."):

            prompt = evaluate_answer(st.session_state.question, answer)

            feedback = ask_nova(prompt)

        st.subheader("AI Feedback")

        st.write(feedback)

# Next question
if st.button("Next Question"):
    st.session_state.question = random.choice(questions)