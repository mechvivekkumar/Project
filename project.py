import streamlit as st
st.title('welcome to ds-free')
name=st.text_input('Enter your name: ')
B=st.button("submit")
if B:
    st.write(f"hi {name},welcome to ds")