import requests
import streamlit as st
from streamlit_lottie import st_lottie

def app():

    def Verifying_url(url):
        r = requests.get(url)
        if r.status_code != 200:
            return None
        return r.json()

    Verify = Verifying_url("https://lottie.host/3245b939-86f3-40ac-8596-5e69a3168dfe/eYqq8XdWCq.json")

    # Create columns, ensure the third column (col3) is set to the far right.
    col1, col2, col3 = st.columns([1, 5, 1])

    # with col1:
    #     st.image("Assets/NCF.png", width=150)

    with col2:
        st_lottie(Verify, height=500, key="rfid")

    # with col3:
    #     st.image("Assets/ICpEP.png", width=150, use_container_width=True)
