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
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

class OptimizeRequest(BaseModel):
    text: str

@app.post("/optimize")
def optimize_text(data: OptimizeRequest):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"Simplify this text for easier reading:\n\n{data.text}"
    )

    return {"optimized_text": response.text}
