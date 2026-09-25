import os

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI

from app.route import router

load_dotenv()

app = FastAPI()

PORT = int(os.getenv("PORT", "8000"))

app.include_router(router)

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=PORT, reload=True)
