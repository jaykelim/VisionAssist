import streamlit as st
from Footer import footer
from pathlib import Path

images_folder = Path("Images")

logo = images_folder / "logo3.png"

st.set_page_config(
    page_title="Vision Assist",
    page_icon="🔭",
)

left_co, cent_co, right_co = st.columns(3)
with cent_co:
    st.image(str(logo))
    st.markdown("""# VisionAssist""")

st.markdown(
    """
    ## 💢 The Challenge
    Navigating the outdoors poses significant challenges for the visually impaired. Traditional aids like canes or guide dogs are invaluable but have limitations in providing information about the environment.

    VisionAssist leverages the capabilities of smart eyewear, equipped with a camera, to take real-time photos of the wearer's surroundings. With the simple push of a button, these images are captured and sent to the VisionAssist app.

    ## 🤔 How It Works 

    * **Capture**: The user initiates a photo capture through their smart eyewear.  
    * **Analysis (GPT-4 Vision)**: Utilizing advanced Generative AI technology, the app processes and analyzes the photo, identifying objects, obstacles, and other critical environmental details.  
    * **Audio Feedback**: The app then verbally describes the scene to the wearer, offering guidance and alerting them to any potential hazards.  
    
    ## ✅ Benefits  

    * **Enhanced Mobility**: Provides a clearer understanding of the surroundings, allowing for safer and more confident navigation.  
    * **Real-Time Information**: Instant feedback ensures up-to-date information about changing environments.  
    * **Accessibility**: Easy to use, with a focus on intuitive design for all users.  

    
"""
)

footer()