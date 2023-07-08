import streamlit as st
import checker
import pickle

model = pickle.load(open('model.pkl','rb'))

st.header('Duplicate question checker')

q1 = st.text_input("Enter First question:")
q2 = st.text_input("Enter Second question:")
q2 = st.text_input("Enter Second question:")

if st.button('Check'):
    query = checker.query_point_creator(q1,q2)
    result = model.predict(query)[0]

    if result:
        st.header('Duplicate')
    else:
        st.header('Not Duplicate')