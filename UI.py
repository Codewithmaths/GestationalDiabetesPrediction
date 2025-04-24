import streamlit as st
import numpy as np
import pickle

# Load the pre-trained model
with open('diabetes1.pkl', 'rb') as file:
    model = pickle.load(file)

# Check the model type for debugging
st.title("Gestational Diabetes")  # This should be a scikit-learn model type

# Validate if the loaded model is correct
if not hasattr(model, 'predict'):
    st.error("The loaded model is not valid. Please check them odel file.")


# Input features
pregnancies = st.number_input("Number of Pregnancies", min_value=0, step=1, format="%d")
glucose = st.number_input("Glucose Level", min_value=0.0, format="%.1f")
blood_pressure = st.number_input("Blood Pressure (mm Hg)", min_value=0.0, format="%.1f")
skin_thickness = st.number_input("Skin Thickness (mm)", min_value=0.0, format="%.1f")
insulin = st.number_input("Insulin Level (IU/mL)", min_value=0.0, format="%.1f")
bmi = st.number_input("BMI (Body Mass Index)", min_value=0.0, format="%.1f")
dpf = st.number_input("Diabetes Pedigree Function", min_value=0.0, format="%.3f")
age = st.number_input("Age (years)", min_value=0, step=1, format="%d")

# Button to make predictions
if st.button("Predict"):
    # Prepare input data
    input_data = np.array([[float(pregnancies), float(glucose), float(blood_pressure), 
                            float(skin_thickness), float(insulin), float(bmi), 
                            float(dpf), float(age)]])


    # Make prediction
    prediction = model.predict(input_data)

    # Display prediction result
    if prediction[0] == 1:
        st.success("The model predicts: Diabetes Positive")
    else:
        st.success("The model predicts: Diabetes Negative")