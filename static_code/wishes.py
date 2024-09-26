import streamlit as st
from PIL import Image
from streamlit_lottie import st_lottie
import json, time

def load_lottie_animation(file_path):
    with open(file_path, "r") as f:
        return json.load(f)

LOTTIE_ANIMATION = "assets/boxmsg.json"

BOX_OPEN_ANIMATION = "assets/letteropen.json"

def show_animation_and_message(message):
    animation_placeholder = st.empty() 

    with animation_placeholder.container():
        box_open_animation = load_lottie_animation(BOX_OPEN_ANIMATION)
        st_lottie(box_open_animation, height=100)
        time.sleep(3.4) 

    animation_placeholder.empty()  
    st.markdown(html_template.format(content=message), unsafe_allow_html=True)


def resize_image(image_path):
    img = Image.open(image_path)
    w, h = img.size
    new_height = int(w * 20 / 15)  
    img_resized = img.resize((w, new_height))
    return img_resized

html_template = """
    <div style="font-family: 'Arial Black', Gadget, sans-serif; font-size: 18px; color: #000000; text-shadow: 1px 1px 1px #FF69B4; background-color: #F0E68C; padding: 9px; border-radius: 10px; max-width: 600px; font-weight: bold;">
        {content}
    </div>
"""

st.markdown(
    """
    <style>
    .stButton button {
        background-color: #6A5ACD; /* Light Slate Blue color */
        color: white;
        border-radius: 6px;
        padding: 8px 16px;
        font-size: 14px;
        font-family: 'Arial', sans-serif; /* Stylish font */
        font-weight: bold;
    }
    .stButton button:hover {
        background-color: #836FFF; /* Lighter shade on hover */
    }
    </style>
    """,
    unsafe_allow_html=True
)

form_data = [
    ("images/dima.jpg", "Mamatha - Your mom"),
    ("images/dipa.jpg", "Bhaskar - Your pa"),
    ("images/pic1.jpg", "Sanjana - Your friend"),
    ("images/difriend.jpg", "Darshan - Your friend"),
    ("images/disanj.jpg", "Thrisha - Your friend")
]


birthday_messages = [
    "Happy Birthday! Wishing you lots of love and happiness.",
    "To the best person in my life, have a fantastic birthday!",
    "Wishing you all the joy and smiles on your special day!",
    "Hope this year brings you everything you've been dreaming of.",
    "Happy Birthday! May your day be as wonderful as you are!"
]

def app():
    
    if 'animation_done' not in st.session_state:
        st.session_state.animation_done = False

    animation_placeholder = st.empty()

    if not st.session_state.animation_done:
        with animation_placeholder.container():
            lottie_animation = load_lottie_animation(LOTTIE_ANIMATION)
            st_lottie(lottie_animation, height=700)
        time.sleep(3.55)
        st.session_state.animation_done = True
        animation_placeholder.empty()

    st.write('')

    for i, (image_path, caption) in enumerate(form_data):
        with st.form(f"form_{i+1}"):  
            st.image(resize_image(image_path), caption=caption, use_column_width=True)
            submitted = st.form_submit_button("Unwrap the Wishes📦🎁")

            
            if submitted:
                show_animation_and_message(birthday_messages[i])

if __name__ == "__main__":
    app()
