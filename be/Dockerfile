# FastAPI 앱을 실행할 Python 베이스 이미지
FROM python:3.10-slim

# 작업 디렉터리 설정
WORKDIR /app

# 의존성 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 소스코드 복사
COPY . .

# 환경변수 설정
ENV PYTHONPATH=/app

# 앱 실행 명령
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
