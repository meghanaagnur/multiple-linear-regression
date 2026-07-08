import streamlit as st
import joblib
import numpy as np
from pathlib import Path

# Load model
BASE_DIR = Path(__file__).resolve().parent
model = joblib.load(BASE_DIR / "model.pkl")

st.set_page_config(
    page_title="House Price Predictor"
)

st.title("House Price Prediction")
st.write(
    "Predict house prices using Multiple Linear Regression."
)

area = st.number_input(
    "Area (sq.ft)",
    min_value=500,
    max_value=10000,
    value=3000
)

bedroom = st.number_input(
    "Number of Bedrooms",
    min_value=1,
    max_value=10,
    value=3
)

age = st.number_input(
    "Age of House (years)",
    min_value=0,
    max_value=100,
    value=20
)

if st.button("Predict Price"):

    prediction = model.predict(
        np.array([[area, bedroom, age]])
    )[0]

    st.success(
        f"Estimated House Price: ${prediction:,.2f}"
    )