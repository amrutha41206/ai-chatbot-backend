from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

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