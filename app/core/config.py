# app/core/config.py

from dotenv import load_dotenv
import os

# .env 파일 읽기
load_dotenv()

# 환경변수 읽기
ADMIN_API_KEY = os.getenv("ADMIN_API_KEY")
