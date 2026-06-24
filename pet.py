import streamlit as st
st.title("🗿MY FUN APP🗿")
name = st.text_input("Enter your name")
mood = st.selectbox("How do you feel?", ["Happy 🙂", "Tired 😴", "Excited😛", "Devilish😈"])
if "visits" not in st.session_state:
    st.session_state.visits = 0

if st.button("Say Hello!"):
    #+= is used to increment
    st.session_state.visits +=1
    st.write(f"hello *{name}*! You feel {mood}")
    st.write(f"You clicked {st.session_state.visits} time(s) today!")

st.image("https://media.giphy.com/media/3o7abKhOpu0NwenH30/giphy.gif", width= 200)

