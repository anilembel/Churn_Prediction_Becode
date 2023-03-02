import streamlit as st
import time
import numpy as np
import pickle

st.title("Churn prediction")
st.markdown("group project for BeCode")

st.header("Our analysis")
st.image("/home/becode/BeCode/projects/05_churn-prediction/Churn_Prediction_Becode/visualizations/Dashboard Analytics.png", use_column_width=True)

st.sidebar.header("Our prediction")
st.sidebar.checkbox("boolean True")
st.sidebar.button("button")
st.sidebar.radio("Pick your gender",["Male","Female"])
st.sidebar.selectbox("Pick your gender",["Male","Female"])
st.sidebar.multiselect("Choose a planet",["Jupiter", "Mars", "neptune"])
st.sidebar.select_slider("Pick a mark", ["Bad", "Good", "Excellent"])
st.sidebar.slider("Pick a number", 0,50)
st.sidebar.number_input("Pick a number", 0,10)
st.sidebar.color_picker("Choose your favorite color")