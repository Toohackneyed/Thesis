import streamlit as st

st.set_page_config(page_title="IdentiTech", page_icon="Assets/Logo.png", layout="wide")
st.markdown(
    """
    <style>
        [data-testid="stMainBlockContainer"] {
            padding: 50px !important;
            background-color: #FFFFFF;
        }
        [data-testid="stHeader"]{
            background-color: "#28A745";
            color: "#FFFFFF";
        }
        [data-testid="stFooter"]{
            visibility: hidden;} 
        [data-testid="stLogo"] {
            top: -10px
            width: 50px;
            height: 50px;
        }
    </style>
    """,
    unsafe_allow_html=True,
)
st.logo("Assets/IdentiTech.png")  # Logo in the sidebar

# Session State to Track Selected Page
if "selected_page" not in st.session_state:
    st.session_state.selected_page = "Home"

navigation_buttons = {
    "🏠 Home": "Home",
    "📅 Attendance": "Attendance",
    "👤 Enrollment": "Enroll User",
    "ℹ️ About App": "About App"
}

for button_text, page_name in navigation_buttons.items():
    if st.sidebar.button(button_text):
        st.session_state.selected_page = page_name

# Map the selected page to the appropriate module
page_modules = {
    "Home": "Home",
    "Attendance": "Profile",
    "Enroll User": "Enroll_User",
    "About App": "About_App",
}

selected = st.session_state.selected_page

if selected in page_modules:
    module_name = page_modules[selected]
    module = __import__(module_name)
    getattr(module, "app" if selected != "About App" else "main")()
