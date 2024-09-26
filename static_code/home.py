import streamlit as st
import time
import io
from pathlib import Path
import json
from streamlit_lottie import st_lottie
from streamlit_extras.let_it_rain import rain
import streamlit.components.v1 as components
from PIL import Image

def app():
    
     
    falling_text_css = """
    <style>
    @keyframes bounce {
        0%, 20%, 50%, 80%, 100% {
            transform: translateY(0);
        }
        40% {
            transform: translateY(-30px);
        }
        60% {
            transform: translateY(-15px);
        }
    }

    @keyframes scale {
        0% { transform: scale(1); opacity: 0; }
        50% { transform: scale(1.5); opacity: 1; }
        100% { transform: scale(1); opacity: 1; }
    }

    @keyframes fall {
        0% { transform: translateY(-100%); opacity: 0; }
        100% { transform: translateY(0); opacity: 1; }
    }

    .animated-text {
        display: inline-block;
        font-size: 2.65em;
        font-weight: bold;
        color: #ff69b4;
        text-shadow: 0 0 10px rgba(255, 105, 180, 0.8), 0 0 20px rgba(255, 105, 180, 0.6);
        margin-top: -13.5px;
    }

    .animated-text span {
        display: inline-block;
        animation: bounce 1s ease infinite, scale 1s ease forwards;
        opacity: 0;
    }

    .animated-text span:nth-child(1) { animation-delay: 0.1s; }
    .animated-text span:nth-child(2) { animation-delay: 0.3s; }
    .animated-text span:nth-child(3) { animation-delay: 0.5s; }
    .animated-text span:nth-child(4) { animation-delay: 0.7s; }
    .animated-text span:nth-child(5) { animation-delay: 0.9s; }
    .animated-text span:nth-child(6) { animation-delay: 1.0s; }
    .animated-text .space { width: 0.25em; display: inline-block; }
    .animated-text span:nth-child(7) { animation-delay: 1.2s; }
    .animated-text span:nth-child(8) { animation-delay: 1.45s; }
    .animated-text span:nth-child(9) { animation-delay: 1.6s; }
    .animated-text span:nth-child(10) { animation-delay: 1.7s; }
    .animated-text span:nth-child(11) { animation-delay: 1.9s; }
    .animated-text span:nth-child(12) { animation-delay: 2.0s; }
    .animated-text span:nth-child(13) { animation-delay: 2.15s; }
    .animated-text span:nth-child(14) { animation-delay: 2.3s; }
    .animated-text span:nth-child(15) { animation-delay: 2.5s; }
    .animated-text span:nth-child(16) { animation-delay: 2.6s; }
    .animated-text span:nth-child(17) { animation-delay: 2.7s; }
    .animated-text span:nth-child(18) { animation-delay: 2.8s; }

    .falling-name {
        display: flex;
        justify-content: center;
        align-items: center;
        font-size: 2.30em;
        font-weight: bold;
        color: #ff69b4;
        text-shadow: 0 0 10px rgba(255, 105, 180, 0.8), 0 0 20px rgba(255, 105, 180, 0.6);
        margin-top: -22px;
    }

    .falling-name span {
        display: inline-block;
        animation: fall 1s ease forwards;
        opacity: 0;
    }

    .falling-name .space { width: 0.5em; display: inline-block; } /* Adjust spacing here */
    
    .falling-name span:nth-child(1) { animation-delay: 2.9s; }
    .falling-name span:nth-child(2) { animation-delay: 2.98s; }
    .falling-name span:nth-child(3) { animation-delay: 3.05s; }
    .falling-name span:nth-child(4) { animation-delay: 3.13s; }
    .falling-name span:nth-child(5) { animation-delay: 3.20s; }
    .falling-name span:nth-child(6) { animation-delay: 3.26s; }
    .falling-name span:nth-child(7) { animation-delay: 3.3s; }
   
    .falling-name span:nth-child(8) { animation-delay: 3.35s; }
    .falling-name span:nth-child(9) { animation-delay: 3.4s; }
    </style>
    """

# Apply the CSS
    st.markdown(falling_text_css, unsafe_allow_html=True)

    # HTML for the animated "Happy Birthday!" text
    falling_text_html = """
    <div class="animated-text">
        <span>H</span><span>a</span><span>p</span><span>p</span><span>y</span><span class="space"></span><span>B</span><span>i</span><span>r</span><span>t</span><span>h</span><span>d</span><span>a</span><span>y</span>
    </div>
    """

    # HTML for the falling "Deekshith" text
    falling_name_html = """
    <div class="falling-name">
        <span>D</span><span>e</span><span>e</span><span>k</span><span>s</span><span>h</span><span>i</span></span><span>t</span><span>h</span>
    </div>
    """
    falling_text_placeholder = st.empty()
    falling_name_placeholder = st.empty()   
    # Display the animated texts
    falling_text_placeholder.markdown(falling_text_html, unsafe_allow_html=True)
    falling_name_placeholder.markdown(falling_name_html, unsafe_allow_html=True)


    time.sleep(4)
    
    image_placeholder = st.empty()

    with image_placeholder.container():
        your_media_file = "static_code/images/di1intro.jpg"
        img = Image.open(your_media_file)
        w, h = img.size
        new_height = int(w * 16 / 15)
        img_resized = img.resize((w, new_height))
        st.image(img_resized)
        
        st.markdown("<b>Solo photo and One liner about him/her ...your  my :red[blahhh]🌍.. and :red[blahhhh]💖", unsafe_allow_html=True)

    
    # Directories & File paths
    this_dir: Path = Path(__file__).parent
    LOTTIE_ANIMATION = this_dir / "assets" / "love_birds.json"
    BOX_OPEN_ANIMATION = this_dir / "assets" / "box_open.json"

    # Load Lottie animations
    def load_lottie_animation(file_path):
        with open(file_path, "r") as f:
            return json.load(f)

    # Animation placeholders
    animation_placeholder = st.empty()
    button_placeholder = st.empty()

    # Run initial bird and heart emoji rain animations
    with animation_placeholder.container():
        rain(emoji="💜", font_size=24, falling_speed=5, animation_length="infinite")
        lottie_animation = load_lottie_animation(LOTTIE_ANIMATION)
        st_lottie(lottie_animation, height=128)


    

    # Button for more surprises
    if button_placeholder.button(" -  🔐A Secret Treat Awaits U! Tap Now🎁"):
        
        button_placeholder.empty()

        with button_placeholder.container():
            animation_placeholder.empty()
            falling_text_placeholder.empty()
            falling_name_placeholder.empty()
            image_placeholder.empty()
        
            box_open_animation = load_lottie_animation(BOX_OPEN_ANIMATION)
            st_lottie(box_open_animation, height=500)
            
            msg = st.toast('🎉Its Celebration Time🎉')
            time.sleep(2.8)
            msg.toast('Are you ready🥳🥳')
            time.sleep(2.2)
            msg.toast('3️⃣')
            time.sleep(1.6)
            msg.toast('2️⃣')
            time.sleep(1.6)
            msg.toast('1️⃣')
            time.sleep(0)
        button_placeholder.empty()

        st.audio('static_code/audio.mp3', autoplay=True )

        def typewriter(text: str, speed: int):
            tokens = text.split()
            container = st.empty()
            
            # HTML template for custom styling
            html_template = """
            <div style="font-family: 'Arial Black', Gadget, sans-serif; font-size: 18px; color: #000000; text-shadow: 1px 1px 1px #FF69B4; background-color: #F0E68C; padding: 9px; border-radius: 10px; max-width: 600px; font-weight: bold;">
                {content}
            </div>
            """
            html_buffer = io.StringIO()
            
            for index in range(len(tokens) + 1):
                curr_full_text = " ".join(tokens[:index])
                container.markdown(html_template.format(content=curr_full_text), unsafe_allow_html=True) 
                html_buffer.write(html_template.format(content=curr_full_text))
                time.sleep(1 / speed)
            
            return html_buffer.getvalue()

        text = """Happy Birthday, Deekshith! 🎉 Wishing you a fantastic day filled with joy, laughter, and all the things that make you happiest. May this year bring you success, good health, and endless reasons to celebrate! 🎂🎈 Keep shining, chasing your dreams, and inspiring those around you. Here's to more adventures, growth, and wonderful memories ahead. Enjoy every moment of your special day and the incredible journey ahead! 🎉"""
        speed = 3
        typewriter(text=text, speed=speed)
        st.write('')
        st.write('')
        st.write("Watch this short video!! 🎥 <b> A glimpse into :red[our incredible journey together🫂🥹❤].", unsafe_allow_html= True )
        video_file = open('static_code/videoo.mp4', 'rb')
        video_bytes = video_file.read()
        st.video(video_bytes)
        st.write('')
        st.write('Think this is it? 🎁 There’s more to discover! Head to the top left corner for extra surprises.')

# Execute the app
if __name__ == "__main__":
    app()
