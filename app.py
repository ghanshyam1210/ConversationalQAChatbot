import streamlit as st
from dotenv import load_dotenv
import os
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-pro")
chat  = model.start_chat(history=[])

## Function to load Google Gemeni Pro model
def get_gemini_response(question) :
    response = chat.send_message(question , stream=True)

    return response

## Initialize streamlit App

st.set_page_config(page_title= "Conversational Q&A Application")
st.header("Google Gemini LLM Application")

# Initialize session state for chat history if it does not present

if 'chat_history' not in st.session_state :
    st.session_state['chat_history'] = []


Input = st.text_input('Input :' , key="input")

submit = st.button("Ask the Question")

if submit and Input :
    response = get_gemini_response(Input)

    ## Store User Question & Response to session chat history

    st.session_state['chat_history'].append(("User" , Input))

    st.subheader("The Response is")

    for chunk in response :
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Bot", chunk.text))

st.subheader("The Chat history is")

for role ,text in st.session_state["chat_history"] :

    st.write(f"{role}:{text}")