# app/core/config.py

from dotenv import load_dotenv
import os
from pydantic_settings import BaseSettings
from typing import Optional

# .env 파일 로드
load_dotenv()

class Settings(BaseSettings):
    PROJECT_NAME: str = "AI Judge"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"
    
    # GitHub API 설정
    GITHUB_TOKEN: Optional[str] = os.getenv("GITHUB_TOKEN")
    
    # 데이터베이스 설정
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./ai_judge.db")
    
    # 보안 설정
    SECRET_KEY: str = os.getenv("SECRET_KEY", "your-secret-key-here")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "11520"))
    
    # 관리자 설정
    ADMIN_API_KEY: Optional[str] = os.getenv("ADMIN_API_KEY")
    
    class Config:
        case_sensitive = True
        env_file = ".env"

settings = Settings()
