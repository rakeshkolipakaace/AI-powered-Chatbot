# GEMINI_API_KEY = "AIzaSyDllhh8PF8P27IFP6B4EGCjJ87wlhu8rUg"  # Replace with your actual Gemini API key
# MONGODB_URI = "mongodb://localhost:27017/"
# DB_NAME = "edu_chatbot"


import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
MONGODB_URI = os.getenv("MONGODB_URI")
DB_NAME = "edu_chatbot"