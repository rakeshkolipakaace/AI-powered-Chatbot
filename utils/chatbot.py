

import google.generativeai as genai
from config.config import GEMINI_API_KEY

try:
   #gpt api   genai.configure(api_key="YOUR_API_KEY")
    # List available models to verify
    available_models = [m.name for m in genai.list_models()]
    print(f"Available models: {available_models}")
    
    # Use a supported model from the list (e.g., gemini-1.5-pro-001)
    model = genai.GenerativeModel('gemini-1.5-pro-001')
except Exception as e:
    raise Exception(f"Failed to configure Gemini API: {str(e)}")

def get_learning_response(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        raise Exception(f"Error generating response: {str(e)}")