import google.generativeai as genai
import os

# Configure API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def generate_gemini_content(transcript_text, prompt):
    """
    Generate a summary using Google Gemini API.
    """
    try:
        model = genai.GenerativeModel("gemini-1.5-flash-latest")
        response = model.generate_content(prompt + transcript_text)
        return response.text
    except Exception as e:
        raise e
