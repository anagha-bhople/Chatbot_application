import streamlit as st
import pandas as pd
from io import StringIO
import os

uploaded_file = st.file_uploader("Choose a file")

def save_uploadedfile(uploadedfile):
    with open(os.path.join("uploaded_files", uploadedfile.name), "wb") as f:
        f.write(uploadedfile.getbuffer())
    return st.success("Saved File:{} to uploaded_files".format(uploadedfile.name))


if uploaded_file is not None:
    save_uploadedfile(uploaded_file)


