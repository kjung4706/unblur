"""
main.py
FastAPI backend service for text optimization.

Handles:
- /optimize endpoint
- Communication with Gemini API
- Prompt construction and response formatting
"""

from fastapi import FastAPI
from pydantic import BaseModel
from google import genai
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
    "http://localhost:5173",
    "https://unblur-reader.vercel.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

class OptimizeRequest(BaseModel):
    text: str

def build_prompt(text: str) -> str:
    """Construct strict prompt to ensure Gemini returns only simplified text
    without explanation, formatting, or markdown."""
    return f"""
        You are a text simplification engine.

        Rewrite the text below to improve readability for a dyslexic reader.

        Rules:
        - Use short sentences.
        - Use simple vocabulary.
        - Avoid complex punctuation.
        - Break long sentences.
        - Keep the original meaning.
        - Do NOT explain your changes.
        - Do NOT add commentary.
        - Return ONLY the rewritten text.

        Text:
        {text}
        """

@app.get("/")
def root():
    return {"message": "unblur api running"}

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/optimize")
def optimize_text(data: OptimizeRequest):
    # Prevent empty submissions
    if not data.text or not data.text.strip():
        return {"optimized_text": ""}
    
    prompt = build_prompt(data.text)

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return {"optimized_text": response.text.strip()}
