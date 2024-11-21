import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title="IdentiTech", page_icon="Assets/Logo.png", layout="wide")

st.markdown(
    """
    <style>
        /* Overall Container Styles */
        [data-testid="stMainBlockContainer"] {
            padding: 0px !important;
            margin: 0px !important;
            background-color: #FFFFFF; /* White background for cleanliness */
        }

        /* Hide Header and Footer */
        [data-testid="stHeader"], [data-testid="stFooter"] {
            visibility: hidden;
        }

        /* Navigation Menu */
        .nav-menu {
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            z-index: 1000;
            background-color: #F5F5F5; /* Light Gray Background for Navbar */
            padding: 0;
            margin: 0;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        }

        /* Content Container */
        .content-container {
            margin-top: 60px; /* Adjust to leave space for the navbar */
            padding: 20px;
            background-color: #FFFFFF;
        }

        /* Header Container */
        .header-container {
            display: flex;
            justify-content: space-between;
            align-items: center;
            width: 100%;
            background-color: #F5F5F5;
            padding: 10px 15px;
            box-shadow: 0px 2px 5px rgba(0, 0, 0, 0.1);
        }

        /* Header Text Styling */
        .header-text {
            font-family: "sans serif";
            font-size: 16px;
            color: #4A4A4A; /* Dark Gray for Readability */
            text-align: center;
        }

        /* Horizontal Line */
        hr {
            border: none;
            height: 2px;
            background-color: #28A745; /* Green Accent */
            margin: 0;
        }

        /* Navigation Bar Highlight Styles */
        .stContainer {
            background-color: #FAFAFA; /* Neutral Background */
        }
         /* Button hover effect with blue */
        .stButton > button:hover {
            background-color: #007BFF !important;  /* Bright blue hover effect */
            color: #FFFFFF !important;  /* White text on hover */
        }

        /* Link hover effect */
        a:hover {
            color: #007BFF !important;  /* Blue for emphasis on hover */
        }

        /* Icon color for active and inactive states */
        .stIcon {
            color: #007BFF !important;  /* Default blue for icons */
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
        "container": {"padding": "10!important", "background-color": "#F5F5F5"},  # Light Gray
        "icon": {"color": "#3498DB", "font-size": "15px"},  # Soft Blue for Icons
        "nav-link": {
            "font-size": "15px",
            "text-align": "center",
            "margin": "0px",
            "--hover-color": "#EAEAEA",  # Soft Gray on Hover
        },
        "nav-link-selected": {"background-color": "#28A745", "color": "white"},  # Green for Selected Item
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
