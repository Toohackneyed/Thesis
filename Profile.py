import streamlit as st
import Admin as Admin

def app():

    @st.dialog("Admin")
    def show_Admin_form():
        Admin.Admin()
    if st.button("Present Admin Form"):
        show_Admin_form()

# if "page_states" not in st.session_state:
#     st.session_state.page_states = {
#         "Home": None,
#         "Attendance": None,
#         "Enroll User": None,
#         "About App": None,
#     }

# if selected == "Home":
#     import Home
#     if st.session_state.page_states["Home"] is None:
#         st.session_state.page_states["Home"] = Home.app()
#     else:
#         Home.app()
# elif selected == "Attendance":
#     import Profile
#     if st.session_state.page_states["Attendance"] is None:
#         st.session_state.page_states["Attendance"] = Profile.app()
#     else:
#         Profile.app()
# elif selected == "Enroll User":
#     import Enroll_User
#     if st.session_state.page_states["Enroll User"] is None:
#         st.session_state.page_states["Enroll User"] = Enroll_User.app()
#     else:
#         Enroll_User.app()
# elif selected == "About App":
#     import About_App
#     if st.session_state.page_states["About App"] is None:
#         st.session_state.page_states["About App"] = About_App.app()
#     else:
#         About_App.app()
# elif selected == "Admin":
#     import Admin
#     if "Admin" not in st.session_state.page_states:
#         st.session_state.page_states["Admin"] = None  # Initialize the key with a default value
#     if st.session_state.page_states["Admin"] is None:
#         st.session_state.page_states["Admin"] = Admin.Admin()
#     else:
#         Admin.Admin()