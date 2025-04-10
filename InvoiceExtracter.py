from dotenv import load_dotenv # type: ignore

load_dotenv()

import streamlit as st # type: ignore
import os 
from PIL import Image # type: ignore
import google.generativeai as genai # type: ignore

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model=genai.GenerativeModel("gemini-2.0-pro-exp")

def get_gemini_response(input,image,prompt):
    response=model.generate_content([input,image[0],prompt])
    return response.text

def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_parts = [
            {
                "inline_data": {
                    "mime_type": uploaded_file.type,
                    "data": bytes_data
                }
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No File Uploaded")


st.set_page_config(page_title="MultiLingual Invoice Extracter")

st.header("Gemini Application")
input=st.text_input("Input Prompt: ",key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg","jpeg","png"])
image=""
if uploaded_file is not None:
    image=Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_container_width=True)

submit=st.button("Tell me about the invoice")

input_prompt="""
You are an expert in understanding invoices. We will upload a image as invoice and you will have to answer any question based on the uploaded invoice image"""


if submit:
    image_data=input_image_setup(uploaded_file)
    response=get_gemini_response(input_prompt,image_data,input)
    st.subheader("The response is")
    st.write(response)