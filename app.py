import streamlit as st
import pickle
import numpy as np
# Load your trained model
model = pickle.load(open("Medical_insurance.pkl", "rb"))

st.title("Medical Insurance Cost Prediction")

# Take user inputs
age = st.number_input("Age", min_value=0, max_value=100, value=25)
bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, value=25.0)
children = st.number_input("Number of Children", min_value=0, max_value=10, value=0)
smoker = st.selectbox("Smoker", ["Yes", "No"])
gender = st.selectbox("Gender", ["Male", "Female"])
region = st.selectbox("Region", ["northeast", "northwest", "southeast", "southwest"])

# Convert inputs into numerical form
smoker_val = 1 if smoker == "Yes" else 0
gender_val = 1 if gender == "Male" else 0

# Example encoding for region (ensure this matches your training data)
region_dict = {"northeast": 0, "northwest": 1, "southeast": 2, "southwest": 3}
region_val = region_dict[region]

# Make prediction
if st.button("Predict Insurance Cost"):
    # Prepare the input data as a 2D array
    input_data = np.array([[age, bmi, children, smoker_val, gender_val, region_val]])
    
    # Predict using the loaded model
    prediction = model.predict(input_data)
    
    # Show result
    st.success(f"Estimated Insurance Cost: ${prediction[0]:,.2f}")
