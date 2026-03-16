import streamlit as st
from nova_client import ask_nova

st.title("📚 Nova Smart Study Assistant")

notes = st.text_area("Paste your notes")

if st.button("Generate Summary"):

    prompt = f"""
Summarize the following study notes clearly for a student:

{notes}
"""

    response = ask_nova(prompt)

    st.subheader("Summary")
    st.write(response)


if st.button("Generate Quiz"):

    prompt = f"""
Create 5 quiz questions based on the following notes:

{notes}
"""

    response = ask_nova(prompt)

    st.subheader("Quiz Questions")
    st.write(response)