import streamlit as st
import pandas as pd
import numpy as np
import pickle
import sklearn


pickle_in = open('randomforestclassifier.pkl','rb')

model = pickle.load(pickle_in)

DevelopedBy:("African Agility Cohort 6")

st.title("Diabetes prediction for pregnant women") 



# inputting a variable


Name = st.text_input("Enter the name")
Pregnancies = st.number_input("Number of times being pregnant:")
Glucose = st.number_input("Amount of Glucose:")         
BloodPressure = st.number_input("BloodPressure:")        
SkinThickness = st.number_input("SkinThickness:")            
Insulin = st.number_input("Insulin:")            
BMI = st.number_input("BMI:")             
DiabetesPedigreeFunction = st.number_input("DiabetesPedigreeFunction:")     
Age =  st.number_input("Age:")         
button=st.button("Predict")
### making prediction
if button:
    Predictions=model.predict([[Pregnancies,Glucose,BloodPressure, SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
    if Predictions == 0:
        st.write("Oooooooops",Name, "is diabetics")
    else:
        st.write(Name, "is not diabetics")
        
        
st.title("DevelopedBy: Africa Agility Cohort 6")
