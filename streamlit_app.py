# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 16:00:58 2023

@author: adarsh
"""

import streamlit as st
import numpy as np
import pickle 

# Remove the deprecated option
# st.set_option('deprecation.showfileUploaderEncoding', False)

with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

# CSS styling
st.markdown(
    """
    <style>
        .main {
            background-color: #044d4d; /* Light Blue */
            padding: 16px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        h2 {
            color: #000;
            text-align: center;
        }
        .footer {
            text-align: center;
            margin-top: 20px;
            font-size: 15px;
            color: #777;
        }
    </style>
    """,
    unsafe_allow_html=True
)

def main():
    html_temp = """
    <div style ="background-color:lightblue;padding:16px">
    <h2 style ='color:black';text-align:center>Adarsh Medical Insurance Cost Predictor App</h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

    with open('model.pkl', 'rb') as file:
        model = pickle.load(file)

    p1 = st.slider("Enter your age", 18, 100)
    s1 = st.selectbox('sex', ('male', 'female'))

    if s1 == 'male':
        p2 = 1
    else:
        p2 = 0

    p3 = st.number_input("Enter your BMI value")
    p4 = st.slider("Enter number of children", 0, 4)
    p5 = st.selectbox("Smoker", ("Yes", "No"))

    if p5 == 'Yes':
        p5 = 1
    else:
        p5 = 0

    p6 = st.slider("Enter your region[select 'southwest':1,'southeast':2,'northwest':3,'northeast':4]", 1, 4)

    if st.button('Predict'):
        pred = model.predict([[p1, p2, p3, p4, p5, p6]])
        st.success('Your insurance cost is {}'.format(round(pred[0], 2)))

    st.markdown(
        "<div class='footer'>Made with ❤️ by Adarsh</div>",
        unsafe_allow_html=True
    )

if __name__ == '__main__':
    main()
