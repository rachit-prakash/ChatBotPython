from dotenv import load_dotenv
load_dotenv() 

import streamlit as st
import os
import google.generativeai as genai
from PIL import Image

# ✅ Load your API key from environment variables (recommended)
genai.configure(api_key="YOUR_API_KEY")

# ✅ Choose a vision-capable model
model = genai.GenerativeModel("gemini-1.5-flash-latest")

def get_gemini_response(input_text, image):
    if input_text:
        response = model.generate_content([
            {"text": input_text},
            image
        ])
    else:
        response = model.generate_content([image])
    return response.text

# ✅ Streamlit UI
st.set_page_config(page_title="Gemini Image Demo")
st.header("Gemini LLM Application")

input_text = st.text_input("Input:", key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

image = None
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_container_width=True)

submit = st.button("Tell me about the image")
if submit:
    if image is not None:
        response = get_gemini_response(input_text, image)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.warning("Please upload an image first.")
