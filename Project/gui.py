import streamlit as st
import numpy as np
import pandas as pd
import pickle
import wikipedia
import requests
import json

# Load in the cleaned dataset
data = pd.read_csv("./data/clean_data.csv")

# Load saved scikit learns models using pickle
polynomial_3_model = pickle.load(open("models/polynomial_3_model.sav", "rb"))

st.title("Prediction of Used Car Auction Sale Prices")
st.text("Brian Smyth - CSE487 Project Final - Spring 2023")

# Webform to accept information from the user
st.header("Enter your car info")
with st.form("Car Info:"):
    make = st.text_input("Make")
    make_search = make.upper()
    model = st.text_input("Model")
    model_search = model.upper()
    year = st.number_input("Model Year", min_value=1900, max_value=2023, value=2023, step=1)
    miles = st.number_input("Mileage", min_value=0, max_value=1000000, value=0, step=1)

    car_search = pd.DataFrame()
    if st.form_submit_button("Predict"):
        car_search = data[data["Make"] == make_search]
        car_search = car_search[car_search["Model"].str.contains(model_search)]
    st.header("Search Results")
    st.text(f"Found {len(car_search)} other results for {make} {model}")

    # Pull car image from wikipedia
    img_url = wikipedia.page(f"{year} {make} {model}").images[0]
    st.image(img_url)
