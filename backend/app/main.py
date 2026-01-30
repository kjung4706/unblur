from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class OptimizeRequest(BaseModel):
    text: str

class OptimizeResponse(BaseModel):
    optimized_text: str


@app.get("/")
def read_root():
    return {"message": "Unblur backend running"}


@app.post("/optimize", response_model=OptimizeResponse)
def optimize_text(request: OptimizeRequest):
    processed = request.text.strip()

    return OptimizeResponse(
        optimized_text=f"Optimized: {processed}"
    )
