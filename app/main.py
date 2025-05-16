# /app/main.py

# 🔹 .env 파일 로드 (가장 먼저)
import os
from dotenv import load_dotenv

load_dotenv()  # .env 환경변수 로딩

# 🔹 FastAPI 프레임워크 및 설정 관련
from fastapi import FastAPI
# 🔹 Swagger 커스텀용
from fastapi.openapi.utils import get_openapi

# 🔹 라우터 불러오기
from app.api.routes import router as api_router

# 🔹 설정값 및 DB 초기화
from app.core.config import settings
from app.db.init_db import init_db

# 🔹 FastAPI 앱 인스턴스 생성
app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION
)

# ✅ DB 테이블 자동 생성
init_db()

# ✅ 모든 API 라우터 일괄 등록
app.include_router(api_router, prefix=settings.API_V1_STR)


# ✅ Swagger UI에 JWT Authorize(🔒) 버튼 추가
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema

    admin_test_token = (
        "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
        ".eyJzdWIiOiJ0ZXN0QGV4YW1wbGUuY29tIiwiZXhwIjoxNzQ5OTYxMTI2fQ"
        ".mrZ0zDpAoceAFb5zyMS-Pi4afAfTpzr9f9Oq30seCVs"
    )

    user_test_token = (
        "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"
        ".eyJzdWIiOiJ1c2VyMUBleGFtcGxlLmNvbSIsImV4cCI6MTc0OTk2MTE3OX0"
        "._FqUJ6DDNU0aHJbeG7iO6X6t-5mAc-CkE58GyEtKxzw"
    )

    openapi_schema = get_openapi(
        title=settings.PROJECT_NAME,
        version=settings.VERSION,
        description=(
            "### 🧠 AI Judge API\n"
            "이 API는 JWT 기반 인증을 사용합니다.\n\n"
            "🔐 테스트용 관리자 토큰 :\n\n"
            f"`{admin_test_token}`"
            "\n\n🔐 테스트용 사용자 토큰 :\n\n"
            f"`{user_test_token}`"
        ),
        routes=app.routes,
    )

    # 🔒 securitySchemes 설정 추가 (JWT Bearer 방식)
    openapi_schema["components"]["securitySchemes"] = {
        "BearerAuth": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT"
        }
    }

    # 모든 API 경로에 security 기본 적용
    for path in openapi_schema["paths"].values():
        for operation in path.values():
            operation.setdefault("security", []).append({"BearerAuth": []})

    app.openapi_schema = openapi_schema
    return app.openapi_schema


# FastAPI에 적용
app.openapi = custom_openapi

# ⚙️ 개발 서버 직접 실행 (터미널에서 python main.py 실행 시)
if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
