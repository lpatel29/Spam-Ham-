import streamlit as st
import joblib
text_model = joblib.load('Email_Class')
st.title('Spam Ham Classifier')
ip = st.text_input('Enter your message')
op = text_model.predict([ip])
if st.button('Predict'):
  st.title(op[0]) 

   
