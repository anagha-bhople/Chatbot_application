import streamlit as st
import streamlit.components.v1 as components
import numpy as np
#components.iframe("https://docs.streamlit.io/en/latest")
import abacusai

import abacusai

client = abacusai.ApiClient('7f1151b7e778426f98e4f156719c2722')
st.title("Custom Bot")

import json
from PyPDF2 import PdfReader

# creating a pdf reader object
reader = PdfReader('/Users/anagha/PycharmProjects/chatbot_application/uploaded_files/first.pdf')

# # printing number of pages in pdf file
# print(len(reader.pages))
#
# for page in reader.pages:
#     # extracting text from page
#     text = page.extract_text()
#     print(text)


# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])


# React to user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    response = f"ROBOT: {prompt}"
    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        st.markdown(response)
    # Add assistant response to chat historySTRE
    st.session_state.messages.append({"role": "assistant", "content": response})