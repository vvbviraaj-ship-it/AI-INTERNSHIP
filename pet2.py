import streamlit as st

num = st.number_input("Enter a number", step=1)

if st.button("Show Table"):
    for i in range(1, 11):
        st.write(f"{num} x {i} = {num*i}")