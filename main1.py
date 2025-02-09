import streamlit as st
import os
from dotenv import load_dotenv
from PIL import Image
import google.generativeai as genai

# Load environment variables
load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Load gemini vision model
model = genai.GenerativeModel('gemini-2.0-flash')

# get response from gemini pro vision model
def gemini_vision_response(model,prompt,image):
    response = model.generate_content([prompt,image])
    return response.text

# Set page title ans icon



st.set_page_config(
    page_title="Chat with Image",
    page_icon="🧠",
    layout="centered"
)

st.title("Chat with Image")

image = st.file_uploader("Upload an image",type=["jpg","png","jpeg"])

user_prompt = st.text_input("Enter your query:")


if st.button("Submit"):
    load_image = Image.open(image)

    colLeft,colRight = st.columns(2)

    with colLeft:
        st.image(load_image.resize((800,500)))

    caption_response = gemini_vision_response(model,user_prompt,load_image)

    with colRight:
        st.info(caption_response)

def set_bg_from_url(url, opacity=1):
    
    footer = """
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-gH2yIJqKdNHPEq0n4Mqa/HGKIhSkIHeL5AyhkYV8i59U5AR6csBvApHHNl/vI1Bx" crossorigin="anonymous">
    <footer>
        <div style='visibility: visible;margin-top:7rem;justify-content:center;display:flex;'>
            <p style="font-size:1.1rem;">
                Powered by Pure AI Lab
                &nbsp;
                </a>
            </p>
        </div>
    </footer>
"""
    st.markdown(footer, unsafe_allow_html=True)
    
    
    # Set background image using HTML and CSS
    st.markdown(
        f"""
        <style>
            body {{
                background: url('{url}') no-repeat center center fixed;
                background-size: cover;
                opacity: {opacity};
            }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Set background image from URL
set_bg_from_url("https://img.freepik.com/premium-vector/chat-vector-icon_676179-133.jpg?w=740", opacity=0.875)