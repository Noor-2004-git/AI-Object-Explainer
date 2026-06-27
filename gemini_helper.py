import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load the .env file
load_dotenv()

# Configure Gemini
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Load the model
model = genai.GenerativeModel("gemini-2.5-flash")


def explain_object(object_name):
    prompt = f"""
    Explain the object '{object_name}' in simple English.

    Include:
    1. What it is
    2. Common uses
    3. One interesting fact

    Keep the response under 80 words.
    """

    response = model.generate_content(prompt)

    return response.text