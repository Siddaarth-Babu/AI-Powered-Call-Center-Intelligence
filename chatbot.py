import os
import speech_recognition as sr
import pyttsx3
from langchain.chains import ConversationChain,LLMChain
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.memory import ConversationBufferMemory,ConversationSummaryMemory
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from template import TEMPLATE

load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")


llm = ChatGoogleGenerativeAI(
    GOOGLE_API_KEY=GOOGLE_API_KEY,
    temperature=0.7,
    model="gemini-1.5-flash"
)

memory = ConversationSummaryMemory(llm=llm,input_key="input")

prompt = PromptTemplate(
    input_variables=["history","input"],
    template=TEMPLATE,
    memory=memory
)


conversation_chain = ConversationChain(
    llm=llm,
    prompt=prompt,
    memory=memory,
    verbose=True
)

speech_recogniser = sr.Recognizer()
engine = pyttsx3.init()

engine.setProperty('rate', 180)
engine.setProperty('volume', 0.9)
engine.setProperty('duration',5)

# def listen() :
#     with sr.Microphone() as source :
#         print("Listening...")
#         audio = speech_recogniser.listen(source)
        
    
#     try :
#         print("Interpreting...")
#         text = speech_recogniser.recognize_google(audio)
#         return text
#     except :
#         print("Could not recognise voice")

# def prompt_response(text) :
#     response = conversation_chain.run({"input" : text})
#     # print(response," func-prompt ",type(response))
#     return response

# def respond(prompt_response) :
#     engine.say(prompt_response)
    
#     engine.runAndWait() #Synchronous execution