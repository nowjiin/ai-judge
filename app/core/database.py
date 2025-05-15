# /app/core/database.py

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.core.config import settings  # ✅ config에서 불러옴

# ✅ SQLAlchemy DB 연결 URL
SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL

# ✅ DB 연결 엔진 생성
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# ✅ 세션 클래스 생성 (자동 커밋/자동 flush 비활성화)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# ✅ 모델들이 상속받을 Base 클래스
Base = declarative_base()


# ✅ FastAPI 종속성 주입용 DB 세션 반환 함수
def get_db():
    """
    FastAPI 라우터에서 사용할 DB 세션을 반환하는 의존성 함수
    사용 후 자동 종료 처리
    """
    db = SessionLocal()
    try:
        yield db  # 의존성 주입
    finally:
        db.close()
