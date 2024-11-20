import streamlit as st
import time

ADMIN_CREDENTIALS = {
    "admin": "securepass"
}

def Admin():
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if not st.session_state.logged_in:
        with st.form("Admin Access"):
            st.subheader("Admin Login")
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            submit_btn = st.form_submit_button("Login")

            if submit_btn:
                if username in ADMIN_CREDENTIALS and password == ADMIN_CREDENTIALS[username]:
                    st.session_state.logged_in = True
                    st.session_state.username = username
                    st.success("Login Successfully!")

                    message_box_placeholder = st.empty()

                    message_box_placeholder.markdown(
                        f'<div style="position: fixed; top: 50%; left: 50%; transform: translate(-50%, -50%); background-color: #f9f9f9; border-radius: 10px; padding: 20px 30px; border: 1px solid #ddd; box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); z-index: 9999; width: auto; text-align: center;">'
                        f'<strong>Welcome, Admin!</strong></div>',
                        unsafe_allow_html=True
                    )
                    time.sleep(3)
                    message_box_placeholder.empty()

                else:
                    st.error("Invalid username or password!")

    if st.session_state.logged_in:
        username = st.session_state.username

        with st.expander("Change Admin Password"):
            old_password = st.text_input("Enter old password", type="password")
            new_password = st.text_input("Enter new password", type="password")
            confirm_password = st.text_input("Confirm new password", type="password")

            change_password_btn = st.button("Change Password")

            if change_password_btn:
                if old_password == ADMIN_CREDENTIALS[username]:
                    if new_password == confirm_password:
                        ADMIN_CREDENTIALS[username] = new_password
                        st.success("Password updated successfully!")
                    else:
                        st.error("New passwords do not match!")
                else:
                    st.error("Old password is incorrect!")

        if st.button("Logout"):
            st.session_state.logged_in = False
            st.session_state.username = None
            st.info("Logged out successfully.")

# Run the Admin function
if __name__ == "__main__":
    Admin()
