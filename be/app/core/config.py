# /app/core/config.py

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # 환경변수에서 읽어올 설정값들 정의
    DATABASE_URL: str
    GITHUB_TOKEN: str = ""
    SECRET_KEY: str

    PROJECT_NAME: str = "AI Judge"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"

    class Config:
        env_file = ".env"  # .env 파일 경로


# 전역에서 불러쓸 수 있게 인스턴스화
settings = Settings()
