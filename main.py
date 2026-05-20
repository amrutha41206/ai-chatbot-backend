from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str

@app.get("/")
def home():
    return {"message": "Backend is running successfully"}

@app.get("/health")
def health():
    return {"status": "success"}

@app.post("/chat")
def chat(request: ChatRequest):
    user_message = request.message
    return {
        "user_message": user_message,
        "bot_reply": f"You said: {user_message}"
    }