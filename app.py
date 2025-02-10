import streamlit as st
import joblib
import numpy as np

# Load the pre-trained model
model = joblib.load('model.joblib')

# Title of the app
st.title('Sonar Rock or Mine Prediction')

# Input from the user
user_input = st.text_input('Enter the input values (comma-separated):')

# Predict button
if st.button('Predict'):
    try:
        # Convert input to numpy array
        input_data = np.array([float(i) for i in user_input.split(',')]).reshape(1, -1)
        
        # Make prediction
        prediction = model.predict(input_data)
        
        # Display result
        if prediction[0] == 0:
            st.success('Prediction: Rock')
        else:
            st.success('Prediction: Mine')
    except Exception as e:
        st.error(f'Error: {e}')