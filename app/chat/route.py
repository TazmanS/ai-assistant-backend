from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from app.chat.dto.chat_request import ChatRequest
from app.chat.service import process_message

router = APIRouter(prefix="/chat")


@router.post("/")
def chat(request: ChatRequest):
    return StreamingResponse(
        process_message(request.message),
        media_type="text/plain",
    )
