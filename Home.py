import streamlit as st

def app():

    st.title("Attendance Monitoring Management System")
    st.markdown("### 'Your attendance, your responsibility. We ensure accuracy.'")

    # Main Section
    st.markdown("""
    Welcome to our Attendance Monitoring System prototype! 
    Our platform provides an easy-to-use solution for tracking attendance efficiently and accurately.
    """)

    # Features Section
    st.markdown("### Key Features")
    st.markdown("""
    - **Real-Time Attendance Tracking**: Easily record attendance in real time.
    - **Automated Reports**: Get detailed reports with just a click.
    - **User-Friendly Dashboard**: Simple and intuitive interface for quick navigation.
    """)

st.markdown('</div>', unsafe_allow_html=True)