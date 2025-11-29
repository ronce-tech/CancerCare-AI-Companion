from fastapi import APIRouter
from pydantic import BaseModel
from app.services.openai_client import get_cancercare_reply

router = APIRouter()

class ChatRequest(BaseModel):
    message: str
    locale: str = "en"
    role: str = "patient"

class ChatResponse(BaseModel):
    reply: str

@router.post("/", response_model=ChatResponse)
async def chat_endpoint(payload: ChatRequest):
    """Simple chat endpoint using a stub AI"""
    reply = await get_cancercare_reply(payload.message, payload.locale, payload.role)
    return ChatResponse(reply=reply)
