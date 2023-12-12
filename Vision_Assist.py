import os
import streamlit as st
from streamlit_image_select import image_select
from dotenv import load_dotenv, find_dotenv
from openai import OpenAI

st.set_page_config(
    page_title="Vision Assist",
    page_icon="🔭",
)


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

