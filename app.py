import os
import speech_recognition as sr
import pyttsx3
import streamlit as st
from chatbot import *

if "messages" not in st.session_state:
        st.session_state.messages = []
# Function to capture voice input
def get_speech_input(placeholder):

    recognizer = sr.Recognizer()
    msg = placeholder.info("Start speaking...")

    with sr.Microphone() as source:
        
        audio = recognizer.listen(source)
        placeholder.info("Interpreting...")
        try:
            text = recognizer.recognize_google(audio)
            msg.empty()
            return text
        except sr.UnknownValueError:
            return "Sorry, I could not understand the audio. Please try again."
        except sr.RequestError:
            return "Sorry, I couldn't process the audio. Please check your microphone or network."


def get_chat_input(user_text) :
    return conversation_chain.run({"input" : user_text})

def setup() :
     # Title of the app
    st.set_page_config(page_title="Bot4Stock", layout="centered",page_icon="https://media.istockphoto.com/id/961649530/vector/finance-graphic-bars-up-rising-arrow-vector-illustration-design.jpg?s=612x612&w=0&k=20&c=sXxosOL8SggL-XNdrm3QP05YFcmTlerS9wqkmB6O-TM=")
    st.image("https://media.istockphoto.com/id/961649530/vector/finance-graphic-bars-up-rising-arrow-vector-illustration-design.jpg?s=612x612&w=0&k=20&c=sXxosOL8SggL-XNdrm3QP05YFcmTlerS9wqkmB6O-TM=",width=50,)
    st.title("AI Bot for Stock Market Investments")

    # Left Sidebar: Description about the bot
    with st.sidebar:
        st.header("About the Bot")
        st.write("""
        Welcome to the AI Bot for Stock Market Investments! I'm here to assist you with:
        - Investment suggestions based on your goals and risk tolerance.
        - Real-time stock performance analysis.
        - Portfolio management advice.
        - Risk management and tax tips.
        Whether you're a beginner or an experienced investor, I'll help guide you through the investment process.
        """)

    # Main user interface
    st.header("How Can I Assist You Today?")
    st.write("You can type your questions or click the microphone button to speak to me directly!")

    # Styling the page for a cool, user-friendly interface
    st.markdown("""
        <style>
        .main {
            
            background: linear-gradient(rgb(38, 51, 61), rgb(50, 55, 65), rgb(33, 33, 78));
            padding: 2rem;
        }
        .sidebar .sidebar-content {
            background-color: #e6f1f7;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            font-size: 16px;
            padding: 10px;
            border-radius: 5px;
        }
        .stButton>button:hover {
            background-color: #45a049;
        }
        </style>
        """, unsafe_allow_html=True)

# Displaying the user input and responding accordingly
def display_util(user_input) :
    with st.chat_message("summary",avatar="https://thumbs.dreamstime.com/b/summary-stamp-label-transparent-background-round-sign-344051788.jpg"):
        st.markdown(memory.load_memory_variables({})['history'])
    
    # st.write(f"You asked: {user_input}")
    st.chat_message("user",avatar="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQRr0YlatAy-hrNCQjzZ7fqDzNiXt7HGmzVaA&s").markdown(user_input)
    bot_response = get_chat_input(user_input)

    with st.chat_message("assistant",avatar="https://i.ibb.co/fSNP7Rz/icons8-chatgpt-512.png"):
            if bot_response:
                st.markdown(bot_response)

    return bot_response

def run() :

    setup()
    # Text input for user question
    user_input = st.text_input("Ask your question or describe your investment needs:")

    if user_input:
        _ = display_util(user_input)

    # Speech-to-text feature with a mic button
    mic_button = st.button("Start Speaking")
    placeholder = st.empty()

    if mic_button:
        response = get_speech_input(placeholder)
        ans = display_util(response)

        engine.say(ans)
        engine.runAndWait() 

if __name__ == '__main__' :
     run()
    


