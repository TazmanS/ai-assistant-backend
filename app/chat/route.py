from fastapi import APIRouter

from app.chat.dto.chat_request import ChatRequest
from app.chat.service import process_message

router = APIRouter(prefix="/chat")


@router.post("/")
def chat(request: ChatRequest):
    response = process_message(request.message)

    return {"message": response}
