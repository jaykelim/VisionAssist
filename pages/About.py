import streamlit as st

st.set_page_config(
    page_title="Vision Assist",
    page_icon="🔭",
)


st.markdown(
    """
    # VisionAssist 🔭 
    
    ### The Challenge
    Navigating the outdoors poses significant challenges for the visually impaired. Traditional aids like canes or guide dogs are invaluable but have limitations in providing information about the environment.

    VisionAssist leverages the capabilities of smart eyewear, equipped with a camera, to take real-time photos of the wearer's surroundings. With the simple push of a button, these images are captured and sent to the VisionAssist app.

    #### 🤔 How It Works 

    * **Capture**: The user initiates a photo capture through their smart eyewear.  
    * **Analysis**: Utilizing advanced Generative AI technology, the app processes and analyzes the photo, identifying objects, obstacles, and other critical environmental details.  
    * **Audio Feedback**: The app then verbally describes the scene to the wearer, offering guidance and alerting them to any potential hazards.  
    
    #### ✅ Benefits  

    * **Enhanced Mobility**: Provides a clearer understanding of the surroundings, allowing for safer and more confident navigation.  
    * **Real-Time Information**: Instant feedback ensures up-to-date information about changing environments.  
    * **Accessibility**: Easy to use, with a focus on intuitive design for all users.  

    #### 🔮 Future Prospects
    With ongoing advancements in AI and wearable technology, VisionAssist has the potential to incorporate more features like facial recognition, sign reading, and even navigation assistance.

    #### 📢 Conclusion
    VisionAssist is not just an application; it's a commitment to inclusivity, independence, and empowerment for the visually impaired community. By bridging the gap between technology and accessibility, we're opening a world of possibilities for those who navigate the world differently.

"""
)

