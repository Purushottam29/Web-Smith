import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_response(prompt: str):
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "system",
                "content": """
            You are a coding assistant.

            Return output ONLY in this JSON format:
            {
                "files": [
                    {
                        "filename": "app.py",
                        "content": "code here"
                    }
                ]
            }

            Do NOT include explanations.
            Do NOT include markdown.
            ONLY return JSON.
            """
                },
                {"role": "user", "content": prompt}
            ]
    )

    return response.choices[0].message.content
