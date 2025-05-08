from fastapi import FastAPI
from app.api.routes import participant, fetch_code
from app.core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
)

# API 라우터 등록
app.include_router(
    participant.router,
    prefix=f"{settings.API_V1_STR}/participants",
    tags=["participants"]
)

app.include_router(
    fetch_code.router,
    prefix=f"{settings.API_V1_STR}",
    tags=["fetch-code"]
)

@app.get("/health")
async def health_check():
    return {"status": "ok"}

# 추후 제거 uvicorn app.main:app --reload
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
