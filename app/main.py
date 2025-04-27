from fastapi import FastAPI
from app.api.v1 import fetch_code

app = FastAPI()

# API 등록
app.include_router(fetch_code.router)

@app.get("/health")
async def health_check():
    return {"status": "ok"}