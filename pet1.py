import streamlit as st

a = st.number_input("First Number")
b = st.number_input("Second Number")

if st.button("Add"):
    st.write("Answer:", a + b)