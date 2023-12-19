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
    ## 🔮 Future Prospects
    With ongoing advancements in AI and wearable technology, VisionAssist has the potential to incorporate more features to improve it's utility and user experience: like facial recognition, sign reading, and even navigation assistance.
    
    #### **1. 🧭 Interactive Navigation Assistance**
    * Integrate real-time GPS-based navigation to provide turn-by-turn directions.
    * Offer route suggestions based on safety, ease of travel, and user preferences.
    
    #### **2.🌎 Language Expansion and Translation Features**
    * Add support for more languages and dialects to cater to a global user base.
    * Include real-time translation features for foreign language signs or announcements.
    
    #### **3.🚉 Integration with Public Transportation Systems**
    * Provide information on public transportation, including schedules, routes, and accessible services.
    * Notify users about delays, changes in services, and the nearest accessible transit options.
    
    #### **4. 🏘 Social and Community Features**
    * Allow users to share their experiences, tips, and routes with a community of VisionAssist users.
    * Include a feature for users to report and share real-time updates on environmental conditions.
    
    #### **5. 👦 Facial Recognition and Personal Interaction**
    * Integrate facial recognition to help users identify known individuals in their vicinity.
    * Notify users when a friend or acquaintance is nearby, facilitating social interactions.

    #### 📢 Conclusion
    VisionAssist is not just an application; it's a commitment to inclusivity, independence, and empowerment for the visually impaired community. By bridging the gap between technology and accessibility, we're opening a world of possibilities for those who navigate the world differently.

"""
)

footer()