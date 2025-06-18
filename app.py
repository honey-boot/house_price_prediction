import streamlit as st
import numpy as np
import pandas as pd
import pickle

# Load model and scaler
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

st.title("🏡 House Price Prediction App")

st.markdown("""
Welcome to the House Price Predictor!  
Please enter the following property details, and we'll predict the house price for you.
""")

# Collect user inputs
bedrooms = st.number_input("Number of Bedrooms", min_value=0, step=1)
bathrooms = st.number_input("Number of Bathrooms", min_value=0.0, step=0.25)
sqft_living = st.number_input("Sqft Living Area", min_value=0)
sqft_lot = st.number_input("Sqft Lot Area", min_value=0)
floors = st.number_input("Number of Floors", min_value=0.0, step=0.5)
waterfront = st.selectbox("Waterfront", [0, 1])
view = st.selectbox("View (0=No view, 4=Excellent)", [0, 1, 2, 3, 4])
condition = st.selectbox("Condition (1=Bad, 5=Excellent)", [1, 2, 3, 4, 5])
grade = st.selectbox("Grade (1=Low, 13=High)", list(range(1, 14)))
sqft_above = st.number_input("Sqft Above", min_value=0)
sqft_basement = st.number_input("Sqft Basement", min_value=0)
yr_built = st.number_input("Year Built", min_value=1800, max_value=2025)
yr_renovated = st.number_input("Year Renovated", min_value=0, max_value=2025)
zipcode = st.number_input("Zipcode", min_value=10000, max_value=99999)
lat = st.number_input("Latitude", format="%.6f")
long = st.number_input("Longitude", format="%.6f")
sqft_living15 = st.number_input("Sqft Living15", min_value=0)
sqft_lot15 = st.number_input("Sqft Lot15", min_value=0)
year = st.number_input("Sale Year", min_value=2000, max_value=2030)
month = st.number_input("Sale Month", min_value=1, max_value=12)
day = st.number_input("Sale Day", min_value=1, max_value=31)

# Predict
if st.button("Predict House Price"):
    input_data = pd.DataFrame([[
        bedrooms, bathrooms, sqft_living, sqft_lot, floors,
        waterfront, view, condition, grade, sqft_above,
        sqft_basement, yr_built, yr_renovated, zipcode, lat,
        long, sqft_living15, sqft_lot15, year, month, day
    ]], columns=[
        'bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot', 'floors',
        'waterfront', 'view', 'condition', 'grade', 'sqft_above',
        'sqft_basement', 'yr_built', 'yr_renovated', 'zipcode', 'lat',
        'long', 'sqft_living15', 'sqft_lot15', 'year', 'month', 'day'
    ])

    # Apply scaling
    input_scaled = scaler.transform(input_data)

    # Predict price
    prediction = model.predict(input_scaled)

    # Output result
    st.success(f"🏠 Predicted House Price: ₹ {prediction[0]:,.2f}")