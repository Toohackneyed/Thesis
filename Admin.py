import streamlit as st

def Admin():
    with st.form("Admin Access"):
        name = st.text_input("Admin")
        email= st.text_input("Password")
        Submit_btn = st.form_submit_button("Login")

        if Submit_btn:
            st.success("Access Granted!")