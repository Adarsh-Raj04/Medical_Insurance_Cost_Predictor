# -*- coding: utf-8 -*-
"""
Created on Sun Apr 16 16:00:58 2023

@author: adarsh
"""

import streamlit as st
import joblib
import numpy as np
import string
import pickle 
st.set_option('deprecation.showfileUploaderEncoding',False)
model = pickle.load(open('new_model.pk1','rb'))
def main():
    html_temp = """
    <div style ="background-color:lightblue;padding:16px">
    <h2 style ='color:black';text-align:center>Health insurance cost predictor</h2>
    </div>
    
    """
    st.markdown(html_temp,unsafe_allow_html=True)
    
    model = joblib.load('model_joblib_gr')
    p1=st.slider("Enter your age",18,100)
    
    s1 = st.selectbox('sex',('male','female'))
    if s1 =='male':
        p2=1
    else:
        p2=0
        
    p3=st.number_input("Enter your BMI value")
    
    p4 = st.slider("Enter number of children",0,4)
    p5=st.selectbox("Smoker",("Yes","No"))
    
    if s1 =='Yes':
        
        p5=1
    else:
        p5=0
        
    p6=st.slider("Enter your region[select 'southwest':1,'southeast':2,'northwest':3,'northeast':4]",1,4)
    
    if st.button('Predict'):
        pred= model.predict([[p1,p2,p3,p4,p5,p6]])
        st.success('Your insurance cost is {}'.format(round(pred[0],2)))
    
    
   
if __name__=='__main__':
    main()
