import google.generativeai as genai
import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
 
load_dotenv()
#get API key
GENAI_API_KEY = os.getenv("GENAI_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

#Initialize llms.
genai.configure(api_key=GENAI_API_KEY)
gemini_model = genai.GenerativeModel('gemini-2.0-flash', generation_config={"temperature": 1}  )
groq_model = ChatGroq(model = 'gemma2-9b-it', groq_api_key = GROQ_API_KEY)

