import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title="IdentiTech", page_icon="Assets/Logo.png", layout="wide")

st.markdown(
    """
    <style>
        [data-testid="stMainBlockContainer"] {
            padding: 0px !important;
            margin: 0px !important;
        }
        [data-testid="stHeader"] {
            visibility: hidden;
        }
        [data-testid="stFooter"] {
            visibility: hidden;
        }
        .nav-menu {
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            z-index: 1000;
            background-color: #fafafa;
            padding: 0;
            margin: 0;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        }
        .content-container {
            margin-top: 0px;
            padding: 0;
        }
        .header-container {
            display: flex;
            justify-content: space-between;
            align-items: center;
            width: 100%;
            background-color: #fafafa;
            padding: 5px 10px;  /* Adds padding to prevent images from going to the edge */
            box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.1);
            margin: 0;
        }
        .header-text {
            font-family: "sans serif";
            font-size: 16px;
            color: #333;
            text-align: center;
            margin: 0 auto;
            padding: 0;
        }
        hr {
            border: none;
            height: 0px;
            background-color: #28A745;
            margin: 0px 0;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

selected = option_menu(
    menu_title=None,
    options=["Home", "Attendance", "Enroll User", "About App", "Admin"],
    icons=["house", "building-add", "person-add", "info-circle", "person-lock"],
    default_index=0,
    orientation="horizontal",
    styles={
        "container": {"padding": "10!important", "background-color": "#fafafa"},
        "icon": {"color": "blue", "font-size": "15px"},
        "nav-link": {
            "font-size": "15px",
            "text-align": "center",
            "margin": "0px",
            "--hover-color": "#eee",
        },
        "nav-link-selected": {"background-color": "#28A745", "color": "black"},
    },
)
st.markdown('<hr>', unsafe_allow_html=True)
st.markdown('<div class="content-container">', unsafe_allow_html=True)

if "page_states" not in st.session_state:
    st.session_state.page_states = {
        "Home": None,
        "Attendance": None,
        "Enroll User": None,
        "About App": None,
    }

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
        st.session_state.page_states["About App"] = About_App.main()
    else:
        About_App.main()
elif selected == "Admin":
    import Admin
    if "Admin" not in st.session_state.page_states:
        st.session_state.page_states["Admin"] = None  # Initialize the key with a default value
    if st.session_state.page_states["Admin"] is None:
        st.session_state.page_states["Admin"] = Admin.Admin()
    else:
        Admin.Admin()

st.markdown('</div>', unsafe_allow_html=True)
