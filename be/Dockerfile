# FastAPI 앱을 실행할 Python 베이스 이미지
FROM python:3.10-slim

# 필요한 시스템 패키지 설치
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/* \

# 작업 디렉터리 생성
WORKDIR /app

# 의존성 복사 및 설치
COPY requirements.txt .
# 가상환경 없이 직접 설치
RUN pip install --no-cache-dir -r requirements.txt

# 소스코드 복사
COPY . .

# 환경변수 설정
ENV PYTHONPATH=/app

# 앱 실행 명령
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
