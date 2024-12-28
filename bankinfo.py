import streamlit as st
import pandas as pd

st.title("File Showcase")

uploader = st.file_uploader("Drag and drop a File: ", type=["csv", "xlsx", "jpg", "png", "json"])
if uploader is not None:
    if uploader.name.endswith(".csv"):
        df = pd.read_csv(uploader, encoding="latin-1")
        st.write(df)
    elif uploader.name.endswith(".xlsx"):
        df = pd.read_excel(uploader)
        st.write(df)
    elif uploader.name.endswith(".jpg") or uploader.name.endswith(".png"):
        st.image(uploader)
    elif uploader.name.endswith(".json"):
        df = pd.read_json(uploader, encoding="latin-1")
        st.write(df)
