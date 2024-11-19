import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title = "IdentiTech", page_icon = "Assets/Logo.png", layout="wide")
st.logo("Assets/IdentiTech.png")
st.markdown(
    """
    <style>
        [data-testid="stMainBlockContainer"] {
            padding: 28px;
            margin: 28px;
        }
        [data-testid="stHeader"] {
            background-color: "rgba(255, 255, 255, 0)";
        }
    </style>
    """,
    unsafe_allow_html=True,
)
col1, col2, col3 = st.columns([1, 11, 1])
with col1:
    st.image("Assets/NCF.png", width=90)
with col3:
    st.image("Assets/ICpEP.png", width=90)

selected = option_menu(menu_title = None,
        options = ["Home", "Attendance", "Enroll User", "About App"],
        icons = ["house", "building-add", "person-add","info-circle"],
        default_index = 0,
        orientation = "horizontal",
        styles={
            "container": {"padding": "0!important", "background-color": "#fafafa"},
            "icon": {"color": "#007BFF", "font-size": "15px"}, 
            "nav-link": {"font-size": "15px", "text-align": "center", "margin":"0px", "--hover-color": "#eee"},
            "nav-link-selected": {"background-color": "#28A745"},
        },
        )

if "page_states" not in st.session_state:
    st.session_state.page_states = {
        "Home": None,
        "Attendance": None,
        "Enroll User": None,
        "About App": None,
    }

# Import and run the selected page
if selected == "Home":
    import Home
    if st.session_state.page_states["Home"] is None:
        st.session_state.page_states["Home"] = Home.app()
    else:
        Home.app()
elif selected == "Attendance":
    import Profile
    if st.session_state.page_states["Attendance"] is None:
        st.session_state.page_states["Attendance"] = Profile.app()
    else:
        Profile.app()
elif selected == "Enroll User":
    import Enroll_User
    if st.session_state.page_states["Enroll User"] is None:
        st.session_state.page_states["Enroll User"] = Enroll_User.app()
    else:
        Enroll_User.app()
elif selected == "About App":
    import About_App
    if st.session_state.page_states["About App"] is None:
        st.session_state.page_states["About App"] = About_App.app()
    else:
        About_App.app()
