import os
import streamlit as st
from streamlit_image_select import image_select
from dotenv import load_dotenv, find_dotenv
from openai import OpenAI

# st.title('Vision Assist')
# load_dotenv(find_dotenv())
# #print(os.environ.get("OPENAI_API_KEY"))

# client = OpenAI()

# caption1 = "Alice, who is visually impaired, approaches a busy urban intersection intent on crossing the street. She senses something unusual across the street but cannot ascertain what it is. Concerned about potential hazards, Alice doesn't want to risk crossing without knowing more about the situation."
# caption2 = "test caption 2"

# img = image_select(
#   label="Select an scenario",
#   images=[
#     "Images\Image1.png",
#     "Images\image2.jpg"
#   ],
#   captions=[caption1, "Second image"]
# )

# if img == "Images\Image1.png":
#   st.write(caption1)
# elif img == "Images\image2.jpg":
#   st.write(caption2)


# st.write(str(img))
# st.image(img)

# completion = client.chat.completions.create(
#     model="gpt-3.5-turbo",
#     messages=[
#         {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
#         {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
#     ]
# )

# if st.button("Analyze Capture"):
#   st.write("Analyzing image.....")

st.set_page_config(
    page_title="Vision Assist",
    page_icon="🔭",
)


st.markdown(
    """
    # VisionAssist 🔭 
    ## Navigating the World with AI-Powered Smart Eyewear
    ### Empowering the Visually Impaired Through Technology
    
    In a world where technology advances at a rapid pace, it's essential that these developments are harnessed to improve the lives of all individuals, including the visually impaired. VisionAssist is a groundbreaking application designed to do just that. Integrated with state-of-the-art smart eyewear, this application aims to revolutionize how visually impaired people interact with their surroundings.

"""
)

