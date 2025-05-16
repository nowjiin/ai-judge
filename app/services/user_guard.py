# /app/services/user_guard.py
# 💡인증된 유저 가져오기 + 역할 검사

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from sqlalchemy.orm import Session
from app.models.user_model import User
from app.core.database import get_db
from app.core.config import settings

import logging

logger = logging.getLogger(__name__)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")


# ✅ 인증된 사용자 가져오기
def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> User:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
    )
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=["HS256"])
        email: str = payload.get("sub")

        if email is None:
            logger.warning("❌ JWT 토큰에서 이메일(sub)을 찾을 수 없음")
            raise credentials_exception
    except JWTError as e:
        logger.warning(f"❌ JWT 디코드 실패: {str(e)}")
        raise credentials_exception

    user = db.query(User).filter(User.email == email).first()
    if user is None:
        logger.warning(f"❌ 토큰은 유효하나 DB에 유저가 없음: {email}")
        raise credentials_exception

    logger.info(f"✅ 인증된 사용자: {user.email} (ID: {user.id})")
    return user


# ✅ 역할 검사 유틸
def require_role(user: User, roles: list[str]):
    if user.role not in roles:
        logger.warning(f"🚫 접근 차단 - 사용자: {user.email}, 현재 역할: {user.role}, 요구 역할: {roles}")
        raise HTTPException(status_code=403, detail="Insufficient role")

    logger.info(f"🔓 역할 인증 통과 - 사용자: {user.email}, 역할: {user.role}")
