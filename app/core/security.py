# /app/core/security.py

from passlib.context import CryptContext
from jose import jwt, JWTError
from datetime import datetime, timedelta
from app.core.config import settings

# ✅ 비밀번호 해싱을 위한 설정 (bcrypt 사용)
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
# ✅ JWT 설정값
SECRET_KEY = settings.SECRET_KEY  # ✅ .env에서 가져온 값
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60  # 토큰 유효 시간 (분)


# ✅ 비밀번호 해싱 함수
def hash_password(password: str) -> str:
    """
    비밀번호를 bcrypt 해시로 변환합니다.
    """
    return pwd_context.hash(password)


# ✅ 비밀번호 검증 함수
def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    입력된 비밀번호와 해싱된 비밀번호가 일치하는지 확인합니다.
    """
    return pwd_context.verify(plain_password, hashed_password)


# ✅ JWT 토큰 생성 함수
def create_access_token(data: dict, expires_delta: timedelta = None) -> str:
    """
    JWT 액세스 토큰을 생성합니다.

    Args:
        data: JWT에 담을 사용자 정보 (예: {"sub": "email@example.com"})
        expires_delta: 유효기간 (기본값: 60분)

    Returns:
        JWT 토큰 문자열
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})  # 만료 시간 추가

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


# ✅ JWT 디코드 함수 (필요할 경우 사용)
def decode_token(token: str) -> dict:
    """
    JWT 토큰을 디코딩하여 payload를 반환합니다.
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise ValueError("Invalid or expired token")
