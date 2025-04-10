# 🤖 Gemini LLM Chatbot Suite with Streamlit

This project contains a collection of **Gemini-powered chatbots** built using **Python** and **Streamlit**, showcasing different capabilities of **Google's Gemini API** including:

- 📄 Text-based Q&A Chatbot
- 💬 Chatbot with history tracking
- 🖼️ Multi-modal chatbot (Image + Text)

Powered by:
- `google.generativeai`
- `streamlit`
- `dotenv`

---

## 🔧 Setup & Installation

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/gemini-chatbot-suite.git
cd gemini-chatbot-suite
2. Create .env File
Create a .env file in the root directory and add your Google Gemini API key:

ini
Copy
Edit
GOOGLE_API_KEY=your_google_gemini_api_key_here
🔒 Never commit .env files to GitHub

3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
If you don't have a requirements.txt, use this:

bash
Copy
Edit
pip install streamlit python-dotenv google-generativeai pillow
🚀 Run the Chatbots
💬 1. Simple Q&A Chatbot
bash
Copy
Edit
streamlit run simple_chatbot.py
Ask a question

Get an instant answer using Gemini LLM

🧠 2. Chatbot with Memory
bash
Copy
Edit
streamlit run chat_with_history.py
Keeps chat history using st.session_state

Gemini responds in a conversational style

🖼️ 3. Image + Text Multi-modal Chatbot
bash
Copy
Edit
streamlit run image_chatbot.py
Upload an image and optionally add a prompt

Gemini describes or analyzes the image

📁 Project Structure
bash
Copy
Edit
├── simple_chatbot.py           # Text-based Q&A
├── chat_with_history.py        # Q&A with chat memory
├── image_chatbot.py            # Image + Text multi-modal
├── .env                        # API key (not included in repo)
├── requirements.txt            # Python dependencies
└── README.md                   # You're reading this!
🧠 Gemini Models Used
gemini-2.0-pro-exp — for advanced text generation

gemini-1.5-flash-latest — for fast, vision-enabled tasks

🛡️ License
MIT License. Free to use and modify for personal or commercial projects.

👨‍💻 Author
Rachit Prakash


🌟 Show Your Support
If you like this project, feel free to ⭐ star the repo or fork it!

yaml
Copy
Edit

---

Let me know if you want:
- A `requirements.txt` auto-generated  
- `.env.example`  
- Deployment instructions for Streamlit Cloud or Hugging Face Spaces  
- Separate folders for each chatbot

Want me to push this to GitHub as a template repo?
