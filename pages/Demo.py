import os
import streamlit as st
from streamlit_image_select import image_select
from dotenv import load_dotenv, find_dotenv
from openai import OpenAI
import base64
from elevenlabs import generate, play, set_api_key, voices

model_purpose = """You are an assistant integrated into a visual assistance application, designed to aid visually impaired individuals in safely navigating urban environments. Your primary function is to interpret and describe images captured by smart eyewear, providing real-time, actionable insights about the user's surroundings."""
model_context = """Analyze the provided image and narrate a concise, clear description focusing on elements crucial for a visually impaired person's safe navigation in an urban setting. Emphasize pedestrian paths, any obstacles or hazards, moving elements like vehicles or people, and relevant signage or traffic signals. Your response should be 3 to 4 sentences, easily audible and understandable, using simple language to aid in quick comprehension and decision-making. """
voices = voices()

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

client = OpenAI()
set_api_key(os.environ.get("ELEVENLABS_API_KEY"))

caption1 = "Alice, who is visually impaired, approaches a busy urban intersection intent on crossing the street. She senses something unusual across the street but cannot ascertain what it is. Concerned about potential hazards, Alice doesn't want to risk crossing without knowing more about the situation."
caption2 = "Sidewalk closed and rerouted"
caption3 = "Van parked blocking pedestrian crosswalk"

img = image_select(
  label="Select a scenario",
  images=[
    "Images\Image1.png",
    "Images\image2.jpg",
    "Images\Image3.png"
  ]
)

if img == "Images\Image1.png":
  st.write(caption1)
elif img == "Images\image2.jpg":
  st.write(caption2)
elif img == "Images\Image3.png":
  st.write(caption3)
  

st.image(img)
response = ""
audio_track = ""
if st.button("Analyze Capture"):
   with st.spinner('Encoding Image....'):
    base64_image = encode_image(str(img))
   with st.spinner('Analyzing Capture....'):
    response = fetch_response(base64_image)
    st.write(response)
   with st.spinner('Generating Audio...'):
    audio_track = generate(response, voice="gfEFZQFYzUcj9hPpmXbd")
    st.audio(audio_track)
   st.success("Done!")

# if st.button("generate audio"):
#   audio_track = generate("Test audio, happy friday everyone", voice="X0kRrWRjGxjEntPwxnnQ")
#   st.audio(audio_track)


