# /app/api/auth/auth_router.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.auth_schema import UserCreate, UserLogin, TokenResponse
from app.services.auth_service import create_user, authenticate_user
from app.core.database import get_db

# FastAPI 라우터 선언
router = APIRouter()


@router.post("/register", response_model=TokenResponse)
def register(user_data: UserCreate, db: Session = Depends(get_db)):
    """
    ✅ 회원가입 API
    - 이메일 중복 체크
    - 비밀번호는 해시 처리
    - 성공 시 JWT 발급
    """
    try:
        token = create_user(db, user_data)
        return {"access_token": token, "token_type": "bearer"}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/login", response_model=TokenResponse)
def login(user_data: UserLogin, db: Session = Depends(get_db)):
    """
    ✅ 로그인 API
    - 이메일, 비밀번호 검증
    - 성공 시 JWT 발급
    """
    token = authenticate_user(db, user_data.email, user_data.password)
    if not token:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"access_token": token, "token_type": "bearer"}
