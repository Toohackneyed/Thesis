import streamlit as st
from Admin import Admin

def app():
    st.title("Enroll User")

@st.dialog("Admin")
def show_Admin_form():
    Admin()
st.write("Enroll User")
if st.button("Enroll"):
    show_Admin_form()