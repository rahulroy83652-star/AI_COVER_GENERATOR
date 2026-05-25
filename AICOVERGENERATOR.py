import streamlit as st

import google.genai as genai

GOOGLE_API_KEY = st.secrets["GOOGLEAPIKEY"]

client = genai.Client(api_key=GOOGLE_API_KEY)
st.title('AI Cover Gnerator')

Job_title = st.text_input("Enter Job Title:")

summary= st.text_input("Enter Resume Summary:")

if st.button("Generate Cover Letter"):
    prompt = f"Write a cover letter for {Job_title} using these resume points: {summary}"
    response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents= prompt)

st.write(response.text)