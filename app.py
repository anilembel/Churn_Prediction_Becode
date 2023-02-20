import streamlit as st
import pandas as pd

st.title("This is the Titel of the web page !")

name = st.text_input("What's your name ?", "")
st.write(f"Hello {name} !")