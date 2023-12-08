import os
import streamlit as st
from streamlit_image_select import image_select
from dotenv import load_dotenv, find_dotenv
from openai import OpenAI
import base64
from elevenlabs import generate, play, set_api_key, voices

model_purpose = """You are an advanced AI model integrated into a visual assistance application, designed to aid visually impaired individuals in safely navigating urban environments. Your primary function is to interpret and describe images captured by smart eyewear, providing real-time, actionable insights about the user's surroundings."""
model_context = """Analyze this image from the perspective of a visually impaired person preparing to navigate an urban environment. Highlight any potential hazards, obstacles, or moving elements, such as vehicles and pedestrians, with a focus on their current activity and position. Provide a clear and detailed description of pedestrian paths, street crossings, and any relevant signage or traffic signals. Emphasize elements critical for safe navigation, using simple and understandable language, and urgently note any immediate dangers or changes in the environment. Ensure the analysis is conciseto allow quick action for the user"""

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def fetch_response(base64_image):
  response = client.chat.completions.create(
    model="gpt-4-vision-preview",
    messages=[
        {
            "role": "system",
            "content": model_purpose,
        },
    ]
    +
    [
        {
            "role": "user",
            "content": [
                    {"type": "text", "text": model_context},
                    {
                        "type": "image_url",
                        "image_url": f"data:image/jpeg;base64,{base64_image}",
                    },
            ],
        },
    ],
    max_tokens=500,
  )
  return response.choices[0].message.content

st.set_page_config(
  page_title="Vision Assist",
  page_icon="🔭",
)

st.title('VisionAssist 🔭')
load_dotenv(find_dotenv())
#print(os.environ.get("OPENAI_API_KEY"))

client = OpenAI()
set_api_key(os.environ.get("ELEVENLABS_API_KEY"))

caption1 = "Alice, who is visually impaired, approaches a busy urban intersection intent on crossing the street. She senses something unusual across the street but cannot ascertain what it is. Concerned about potential hazards, Alice doesn't want to risk crossing without knowing more about the situation."
caption2 = "test caption 2"

img = image_select(
  label="Select an scenario",
  images=[
    "Images\Image1.png",
    "Images\image2.jpg"
  ]
)

if img == "Images\Image1.png":
  st.write(caption1)
elif img == "Images\image2.jpg":
  st.write(caption2)


st.write(str(img))
st.image(img)
response = ""
audio_track = ""
if st.button("Analyze Capture"):
   with st.spinner('Encoding Image....'):
    base64_image = encode_image(str(img))
   with st.spinner('Analyzing Capture....'):
    response = fetch_response(base64_image)
   with st.spinner('Generating Audio...'):
    audio_track = 
   st.success("Done!")

st.write(response)
#t.audio()
