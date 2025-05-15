# /app/models/user_model.py

from sqlalchemy import Column, Integer, String
from app.core.database import Base


# ✅ SQLAlchemy 모델: users 테이블 정의
class User(Base):
    __tablename__ = "users"  # 실제 DB에 생성될 테이블 이름

    id = Column(Integer, primary_key=True, index=True)  # 고유 ID
    username = Column(String(50), nullable=False)       # 사용자 이름
    email = Column(String(100), unique=True, index=True, nullable=False)  # 이메일 (중복 금지)
    hashed_password = Column(String(255), nullable=False)  # 해싱된 비밀번호
    role = Column(String(20), default="user")           # 사용자 역할 (예: "judge", "admin")
