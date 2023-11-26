# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 16:00:58 2023

@author: adarsh
"""

import streamlit as st
import numpy as np
import pickle

# Load the model outside the main function
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

# CSS styling
st.markdown(
    """
    <style>
        .main {
            background-color: #f0f8ff; /* Light Blue */
            padding: 16px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        h2 {
            color: black;
            text-align: center;
        }
        .footer {
            text-align: center;
            margin-top: 20px;
            font-size: 12px;
            color: #777;
        }
    </style>
    """,
    unsafe_allow_html=True
)

def main():
    st.markdown("<h2>Health Insurance Cost Predictor</h2>", unsafe_allow_html=True)

    p1 = st.slider("Enter your age", 18, 100)
    
    s1 = st.radio('Select gender', ('Male', 'Female'))
    p2 = 1 if s1 == 'Male' else 0
    
    p3 = st.number_input("Enter your BMI value", format="%f", step=0.1)

    p4 = st.slider("Enter number of children", 0, 4)
    
    p5 = st.selectbox("Are you a smoker?", ("No", "Yes"))
    p5 = 1 if p5 == 'Yes' else 0

    p6 = st.slider(
        "Select your region",
        options=["Southwest", "Southeast", "Northwest", "Northeast"],
        value=1,
    )

    if st.button('Predict'):
        pred = model.predict([[p1, p2, p3, p4, p5, p6]])
        st.success('Your estimated insurance cost is ${:.2f}'.format(pred[0]))

    st.markdown(
        "<div class='footer'>Made with ❤️ by Adarsh</div>",
        unsafe_allow_html=True
    )

if __name__ == '__main__':
    main()
