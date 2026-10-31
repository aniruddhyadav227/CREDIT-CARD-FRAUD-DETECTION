import streamlit as st
import joblib
import numpy as np
from utils import save_prediction

# Model load karna (models folder se)
try:
    model = joblib.load('models/fraud_model.pkl')
except FileNotFoundError:
    st.error("Model file 'models/fraud_model.pkl' nahi mili. Pehle model train karein.")

st.title("💳 Credit Card Fraud Detection System")
st.write("Machine Learning aur PostgreSQL ke saath real-time prediction.")

# User Inputs (Example features based on standard Kaggle dataset)
amount = st.number_input("Transaction Amount ($)", min_value=0.0, value=150.0)
time = st.number_input("Time (Seconds from first transaction)", value=0.0)
v1 = st.number_input("V1 Feature (PCA)", value=0.0)
v2 = st.number_input("V2 Feature (PCA)", value=0.0)

if st.button("Predict Fraud"):
    # Input data ko array mein convert karna
    input_data = np.array([[time, v1, v2, amount]])
    
    # Prediction karna
    prediction = model.predict(input_data)[0]
    
    if prediction == 1:
        st.error("🚨 WARNING: Fraudulent Transaction Detected!")
        save_prediction((amount, time, v1, v2), True)
    else:
        st.success("✅ Transaction is Safe/Legit.")
        save_prediction((amount, time, v1, v2), False)