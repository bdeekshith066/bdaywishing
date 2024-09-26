from flask import Flask, request, jsonify, render_template
import requests
import base64
import os

app = Flask(__name__)

# Use environment variables for GitHub credentials
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
GITHUB_USER = os.getenv('GITHUB_USER')

headers = {
    'Authorization': f'token {GITHUB_TOKEN}',
    'Accept': 'application/vnd.github.v3+json'
}

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/create-repo', methods=['POST'])
def create_repo():
    data = request.json
    repo_name = data['repoName']
    nickname = data['nickname']  # Get the nickname from the user input

    # Step 1: Create the GitHub repository
    create_repo_url = 'https://api.github.com/user/repos'
    repo_data = {
        'name': repo_name,
        'private': False
    }

    response = requests.post(create_repo_url, json=repo_data, headers=headers)
    if response.status_code == 201:
        repo_url = f'https://api.github.com/repos/{GITHUB_USER}/{repo_name}/contents'

        # Step 2: Prepare the static files content (main.py, home.py, chatbot.py, wishes.py)
        # Dynamically replace {nickname} with the user's nickname in main.py
        files_content = {
            'main.py': f'''
import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_extras.let_it_rain import rain
import streamlit.components.v1 as components
import home, chatbot, wishes
from streamlit_extras.app_logo import add_logo
from PIL import Image

# Reducing whitespace on the top of the page
st.markdown(\"\"\"
<style>
.block-container {{
    padding-top: 1rem;
    padding-bottom: 0rem;
    margin-top: 1rem;
}}
</style>
\"\"\", unsafe_allow_html=True)

class MultiApp:
    def __init__(self):
        self.app = []

    def add_app(self, title, func):
        self.app.append({{
            "title": title,
            "function": func
        }})

    def run(self):
        with st.sidebar:
            st.markdown(\"\"\"
            `<style>
            .gradient-text {{
              margin-top: -20px;
            }}
            </style>
            \"\"\", unsafe_allow_html=True)

            typing_animation = f\"\"\"<h3 style="text-align: left;">
            <img src="https://readme-typing-svg.herokuapp.com/?font=Righteous&size=50&Left=true&vLeft=true&width=500&height=70&lines=🍾HBD+{nickname}" alt="Typing Animation" />
            </h3>\"\"\"
            st.markdown(typing_animation, unsafe_allow_html=True)

            app = option_menu(
                menu_title='Sections',
                options=['Home❤','Nostalgia Narrator✍️', 'WishBox📦'],
                default_index=0,
            )
            st.write('')

            your_media_file = "images/dicouple.jpg"
            img = Image.open(your_media_file)
            w, h = img.size
            new_height = int(w * 16 / 15)
            img_resized = img.resize((w, new_height))
            st.sidebar.image(img_resized, caption="couple pic")

        if app == "Home❤":
            home.app()

        elif app == 'Nostalgia Narrator✍️':
            chatbot.app()

        elif app == 'WishBox📦':
            wishes.app()

# Create an instance of the MultiApp class and run the app
MultiApp().run()
            ''',

            'home.py': '''
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
    falling_text_css = \"\"\"
    <style>
    @keyframes bounce {{
        0%, 20%, 50%, 80%, 100% {{
            transform: translateY(0);
        }}
    </style>
    \"\"\"
            ''',

            'chatbot.py': '''
import streamlit as st

st.markdown(\"\"\"<style>
.block-container {{
    padding-top: 1rem;
    padding-bottom: 0rem;
    margin-top: 1rem;
}}
</style>\"\"\", unsafe_allow_html=True)

def app():
    gradient_text_html = \"\"\"
        <style>
        .gradient-text {{
        }}
        </style>
    \"\"\"
            ''',

            'wishes.py': '''
import streamlit as st
from PIL import Image
from streamlit_lottie import st_lottie
import json, time

# Function to load Lottie animation JSON
def load_lottie_animation(file_path):
    with open(file_path, "r") as f:
        return json.load(f)
    
# Load the box animation
LOTTIE_ANIMATION = "assets/boxmsg.json"
# Load the box open animation
BOX_OPEN_ANIMATION = "assets/letteropen.json"
            '''
        }

        # Step 3: Push main files to the GitHub repository
        for filename, content in files_content.items():
            content_base64 = base64.b64encode(content.encode()).decode()
            file_data = {
                'message': f'Add {filename}',
                'content': content_base64
            }
            file_response = requests.put(f'{repo_url}/{filename}', json=file_data, headers=headers)
            if file_response.status_code != 201:
                return jsonify({'message': f'Error creating {filename} in the repository'}), 500

        # Step 4: Add the four JSON files to the assets folder
        assets_files_content = {
            'box_open.json': '{"v":"4.6.0","meta":{"g":"LottieFiles AE 3.1.1"},"fr":36,"ip":0,"op":30,"w":640,"h":480,"nm":"Party Gifts","ddd":0}',
            'boxmsg.json': '{"v":"4.7.0","meta":{"g":"LottieFiles AE 3.1.1"},"fr":37,"ip":0,"op":30,"w":640,"h":480,"nm":"Party Gifts","ddd":0}',
            'letteropen.json': '{"v":"4.8.0","meta":{"g":"LottieFiles AE 3.1.1"},"fr":38,"ip":0,"op":30,"w":640,"h":480,"nm":"Party Gifts","ddd":0}',
            'love_bird.json': '{"v":"4.9.0","meta":{"g":"LottieFiles AE 3.1.1"},"fr":39,"ip":0,"op":30,"w":640,"h":480,"nm":"Party Gifts","ddd":0}'
        }

        for filename, content in assets_files_content.items():
            content_base64 = base64.b64encode(content.encode()).decode()
            file_data = {
                'message': f'Add {filename}',
                'content': content_base64
            }
            file_response = requests.put(f'{repo_url}/assets/{filename}', json=file_data, headers=headers)
            if file_response.status_code != 201:
                return jsonify({'message': f'Error creating {filename} in the assets folder'}), 500

        return jsonify({'message': 'Repository created successfully'}), 201
    else:
        return jsonify({'message': 'Error creating repository'}), 500


if __name__ == '__main__':
    app.run(debug=True)
