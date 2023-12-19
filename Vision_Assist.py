import os
import streamlit as st
from streamlit_image_select import image_select
from dotenv import load_dotenv, find_dotenv
from openai import OpenAI
from Footer import footer

def add_logo(img_path):
    st.markdown(
        """
        <style>
            [data-testid="stSidebarNav"] {
                background-image: "Images\logo3.png";
                background-repeat: no-repeat;
                padding-top: 120px;
                background-position: 20px 20px;
            }
            [data-testid="stSidebarNav"]::before {
                content: "My Company Name";
                margin-left: 20px;
                margin-top: 20px;
                font-size: 30px;
                position: relative;
                top: 100px;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

st.set_page_config(
    page_title="Vision Assist",
    page_icon="🔭",

)

#st.sidebar.image("Images\logo3.png", use_column_width=True)
#add_logo("Images\logo3.png")

left_co, cent_co, right_co = st.columns(3)
with cent_co:
    st.image("Images\logo3.png")
    st.markdown("""# VisionAssist""")


st.markdown(
    """
    ## Navigating the World with AI-Powered Smart Eyewear
    ### Empowering the Visually Impaired Through Technology
    
    In a world where technology advances at a rapid pace, it's essential that these developments are harnessed to improve the lives of all individuals, including the visually impaired. VisionAssist is a groundbreaking application designed to do just that. Integrated within state-of-the-art smart eyewear, this application aims to revolutionize how visually impaired people interact with their surroundings.

"""
)

footer()
