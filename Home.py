import base64
import streamlit as st

@st.cache_data
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

def app():
    # Load the background image
    image = get_base64_of_bin_file('Assets/bg.jpg')

    # Apply CSS for the app's background and text styling
    st.markdown(
        f"""
        <style>
        [data-testid="stHeader"] {{
            visibility: hidden;

        }}

        .stApp {{
            background-image: url("data:image/jpg;base64,{image}");
            background-size: cover;
            background-position: center;
            color: "#4A4A4A";
        }}

        .framed-content {{
            background-color: rgba(0.7216, 0.8863, 0.9490, 0.1);
            padding: 15px;
            border-radius: 10px;
            font-style: sans serif;
            font-size: 18px;
            text-align: center;
            width: 100%;
            margin: auto;
            margin-top: 15px;
        }}
        </style>

        <!-- Render all text inside a framed container -->
        <div class="framed-content">
            <h1>Your attendance, your responsibility. We ensure accuracy</h1>
            <b>Welcome to our Attendance Monitoring System prototype!</b>
            <p>
                Our platform provides an easy-to-use solution for tracking attendance 
                efficiently and accurately.
            </p>
            <h3>Key Features</h3>
            <ul>
                <li>Real-Time Attendance Tracking: Easily record attendance in real time.</li>
                <li>Automated Reports: Get detailed reports with just a click.</li>
                <li>User-Friendly Dashboard: Simple and intuitive interface for quick navigation.</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )

# Run the app
app()
