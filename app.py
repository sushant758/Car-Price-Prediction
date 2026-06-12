import streamlit as st
import pickle
import pandas as pd
import numpy as np

# Load model
with open("car_price_model .pkl", "rb") as file:
    model = pickle.load(file)

st.title("🚗 Car Price Prediction App")

# Inputs
year = st.number_input("Manufacturing Year", min_value=1992, max_value=2025, value=2018)

km_driven = st.number_input("KM Driven", min_value=0, value=50000)

transmission = st.selectbox(
    "Transmission",
    ["Manual", "Automatic"]
)

brand = st.selectbox(
    "Brand",
    [
        "Audi","Bmw","Chevrolet","Datsun","Fiat","Ford","Honda",
        "Hyundai","Mahindra","Maruti","Mercedes-Benz","Nissan",
        "Renault","Skoda","Tata","Toyota","Volkswagen","Other"
    ]
)

fuel = st.selectbox(
    "Fuel Type",
    ["Petrol","Diesel","CNG","Electric","LPG"]
)

owner = st.selectbox(
    "Owner Type",
    [
        "First Owner",
        "Second Owner",
        "Third Owner",
        "Fourth & Above Owner",
        "Test Drive Car"
    ]
)

seller_type = st.selectbox(
    "Seller Type",
    [
        "Individual",
        "Dealer",
        "Trustmark Dealer"
    ]
)

# Predict button
if st.button("Predict Price"):

    car_age = 2025 - year

    data = {
        'km_driven': np.log1p(km_driven),
        'transmission': 1 if transmission == "Automatic" else 0,
        'car_age': car_age
    }

    # Fuel
    for f in ['CNG','Diesel','Electric','LPG','Petrol']:
        data[f'fuel_{f}'] = 1 if fuel == f else 0

    # Seller Type
    for s in ['Dealer','Individual','Trustmark Dealer']:
        data[f'seller_type_{s}'] = 1 if seller_type == s else 0

    # Owner
    for o in [
        'First Owner',
        'Fourth & Above Owner',
        'Second Owner',
        'Test Drive Car',
        'Third Owner'
    ]:
        data[f'owner_{o}'] = 1 if owner == o else 0

    # Brands
    brands = [
        'Audi','Bmw','Chevrolet','Datsun','Fiat','Ford',
        'Honda','Hyundai','Mahindra','Maruti',
        'Mercedes-Benz','Nissan','Other',
        'Renault','Skoda','Tata','Toyota','Volkswagen'
    ]

    for b in brands:
        data[f'name_{b}'] = 1 if brand == b else 0

    input_df = pd.DataFrame([data])

    prediction = model.predict(input_df)[0]

    # Reverse log transform
    predicted_price = np.expm1(prediction)

    st.success(f"Estimated Price: ₹ {predicted_price:,.0f}")