
import pandas as pd
import streamlit as st

st.title("Employee Compensation Forecasting App")
st.write("Upload employee data to begin analysis.")
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write(df.describe())
