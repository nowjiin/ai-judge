# /app/services/auth_service.py

from sqlalchemy.orm import Session
from app.models.user_model import User
from app.schemas.auth_schema import UserCreate
from app.core.security import hash_password, verify_password, create_access_token


# ✅ 회원가입 로직
def create_user(db: Session, user_data: UserCreate) -> str:
    """
    사용자를 DB에 저장하고 JWT 토큰을 생성합니다.

    Args:
        db (Session): DB 세션
        user_data (UserCreate): 사용자 입력 정보

    Returns:
        str: JWT access token
    """
    # 이메일 중복 확인
    existing_user = db.query(User).filter(User.email == user_data.email).first()
    if existing_user:
        raise ValueError("Email already registered")

    # 비밀번호 해시화
    hashed_pw = hash_password(user_data.password)

    # User 객체 생성
    new_user = User(
        # ✅ 사용자 이름
        username=user_data.username,
        # ✅ 이메일 = ID
        email=user_data.email,
        # ✅ 비밀번호
        hashed_password=hashed_pw,
        # ✅ 역할 부여
        role="user"
    )

    # DB에 저장
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    # JWT 토큰 생성
    return create_access_token({"sub": new_user.email})


# ✅ 로그인 로직
def authenticate_user(db: Session, email: str, password: str) -> str | None:
    """
    이메일과 비밀번호를 검증하고 JWT 토큰을 반환합니다.

    Returns:
        str | None: 성공 시 토큰, 실패 시 None
    """
    # 이메일로 사용자 조회
    user = db.query(User).filter(User.email == email).first()
    if not user:
        return None

    # 비밀번호 확인
    if not verify_password(password, user.hashed_password):
        return None

    # 로그인 성공 → JWT 토큰 반환
    return create_access_token({"sub": user.email})
