import streamlit as st
import numpy as np
import pickle

# Load the model once at startup
with open('best_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Streamlit UI
st.title("Simple Prediction App")
st.write("Enter feature values and get a prediction.")

# Input fields
feature1 = st.number_input("Feature 1", value=0.0)
feature2 = st.number_input("Feature 2", value=0.0)
feature3 = st.number_input("Feature 3", value=0.0)
feature4 = st.number_input("Feature 4", value=0.0)

if st.button("Predict"):
    try:
        features = np.array([feature1, feature2, feature3, feature4]).reshape(1, -1)
        prediction = model.predict(features)[0]
        st.success(f"Prediction: {prediction}")
    except Exception as e:
        st.error(f"Error: {str(e)}")
