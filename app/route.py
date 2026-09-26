from fastapi import APIRouter

from app.chat.route import router as chat_router
from app.health.route import router as health_router

router = APIRouter(prefix="/api")

router.include_router(health_router)
router.include_router(chat_router)
