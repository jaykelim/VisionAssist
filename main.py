import os
import streamlit as st
from streamlit_image_select import image_select
from dotenv import load_dotenv, find_dotenv
from openai import OpenAI

st.title('Vision Assist')
load_dotenv(find_dotenv())
#print(os.environ.get("OPENAI_API_KEY"))

client = OpenAI()

img = image_select(
  label="Select an image",
  images=[
    "Images\Image1.png",
    "Images\image2.jpg"
  ],
  captions=["First image", "Second image"]
)

st.write(str(img))
st.image(img)

# completion = client.chat.completions.create(
#     model="gpt-3.5-turbo",
#     messages=[
#         {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
#         {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
#     ]
# )

if st.button("Analyze Capture"):
  st.write("Analyzing image.....")

