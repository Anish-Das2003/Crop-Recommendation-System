import streamlit as st
import numpy as np
import pandas as pd
import pickle

# ----------------------------------
# Load encoder, scaler, and model
# ----------------------------------
encoder = pickle.load(open("models/encoder.pkl", "rb"))
scaler = pickle.load(open("models/scaler.pkl", "rb"))
model = pickle.load(open("models/model_gbc.pkl", "rb"))

# ----------------------------------
# Streamlit Page Config
# ----------------------------------
st.set_page_config(
    page_title="Crop Recommendation System",
    page_icon="🌱",
    layout="centered"
)

st.title("🌱 Crop Recommendation System")
st.write("Enter soil and climate details to get the best crop recommendation.")

# ----------------------------------
# User Inputs
# ----------------------------------
col1, col2 = st.columns(2)

with col1:
    N = st.number_input("Nitrogen (N)", min_value=0.0, step=1.0)
    P = st.number_input("Phosphorus (P)", min_value=0.0, step=1.0)
    K = st.number_input("Potassium (K)", min_value=0.0, step=1.0)
    temperature = st.number_input("Temperature (°C)", step=0.1)

with col2:
    humidity = st.number_input("Humidity (%)", step=0.1)
    ph = st.number_input("pH value", step=0.1, max_value=10.0)
    rainfall = st.number_input("Rainfall (mm)", step=0.1)

# ----------------------------------
# Prediction Button
# ----------------------------------
if st.button("🌾 Predict Best Crop"):
    # Create DataFrame (IMPORTANT: same column names as training)
    input_df = pd.DataFrame(
        [[N, P, K, temperature, humidity, ph, rainfall]],
        columns=['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall']
    )

    # Scale input
    input_scaled = scaler.transform(input_df)

    # Predict
    prediction_encoded = model.predict(input_scaled)
    prediction = encoder.inverse_transform(prediction_encoded)

    # Output
    st.success(f"✅ Recommended Crop: **{prediction[0]}**")

# ----------------------------------
# Footer
# ----------------------------------
st.markdown("---")
st.caption("🚜 Machine Learning based Crop Recommendation System")