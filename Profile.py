import streamlit as st
import Admin as Admin

def app():

    # Create two columns, one for the button on the right
    col1, col2 = st.columns([1, 2])  # Adjust the ratio for layout

    with col2:  # Place the button in the second column (right side)
        if st.button("Present Admin Form"):
            @st.dialog("Admin")
            def show_Admin_form():
                Admin.Admin()
            show_Admin_form()
            

            

    
