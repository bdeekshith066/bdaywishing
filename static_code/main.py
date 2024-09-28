import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_extras.let_it_rain import rain
import streamlit.components.v1 as components
import  home, chatbot, wishes
from streamlit_extras.app_logo import add_logo
from PIL import Image

st.markdown("""
<style>

.block-container
{
    padding-top: 1rem;
    padding-bottom: 0rem;
    margin-top: 1rem;
}

</style>
""", unsafe_allow_html=True)

class MultiApp:
    def __init__(self):
        self.app = []

    def add_app(self, title, func):
        self.app.append({
            "title": title,
            "function": func
        })   

    def run(self):  
        with st.sidebar:     
            
            
            
            typing_animation = """
            <h3 style="text-align: left;">
            <img src="https://readme-typing-svg.herokuapp.com/?font=Righteous&size=50&Left=true&vLeft=true&width=500&height=70&lines=🍾HBD+Dixitt!!" alt="Typing Animation" />
            </h3>
            """
            st.markdown(typing_animation, unsafe_allow_html=True)
            
            app = option_menu(
                menu_title='Sections',
                options=['Home❤','Nostalgia Narrator✍️', 'WishBox📦'],
                default_index=0,
                icons=['house', 'book', 'box'],
                menu_icon="cast",
                orientation="vertical",

            )
            st.write('')
            
            your_media_file = "static_code/images/sidebar.jpg"  
            img = Image.open(your_media_file)
            w, h = img.size
            new_height = int(w * 16 / 15)
            img_resized = img.resize((w, new_height))
            st.sidebar.image(img_resized , caption = "I love you Deekshith!")


        if app == "Home❤":
            home.app()
        
        elif app == 'Nostalgia Narrator✍️':
            chatbot.app()
        
        elif app == 'WishBox📦':
            wishes.app()

# Create an instance of the MultiApp class and run the app
MultiApp().run()
