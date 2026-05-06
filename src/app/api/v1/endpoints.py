from fastapi import APIRouter
from pydantic import BaseModel
from app.services.chat_logic import generate_response

router = APIRouter()

class ChatRequest(BaseModel):
    message: str

@router.post("/chat")
def chat(request: ChatRequest):
    reply = generate_response(request.message)
    return {"reply": reply}
