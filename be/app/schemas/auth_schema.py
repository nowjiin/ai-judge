# /app/schemas/auth_schema.py

from pydantic import BaseModel, EmailStr


# ✅ 회원가입 요청 시 사용되는 요청 모델
class UserCreate(BaseModel):
    username: str            # 사용자 이름
    email: EmailStr          # 이메일 (형식 자동 검증됨)
    password: str            # 비밀번호


# ✅ 로그인 요청 시 사용되는 요청 모델
class UserLogin(BaseModel):
    email: EmailStr          # 로그인용 이메일
    password: str            # 비밀번호


# ✅ JWT 토큰 응답 형식
class TokenResponse(BaseModel):
    access_token: str        # JWT 액세스 토큰
    token_type: str = "bearer"  # 토큰 타입 (일반적으로 "bearer")
