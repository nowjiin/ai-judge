# /app/api/auth/check_role.py
# 역할 확인, 역할 부여 등 권한 관련 API

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.services.user_guard import get_current_user
from app.models.user_model import User

router = APIRouter()


@router.get("/get_role")
def get_my_role(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    ✅ 현재 로그인된 유저의 role(역할)을 반환하는 API
    """
    return {
        "id": current_user.id,
        "username": current_user.username,
        "email": current_user.email,
        "role": current_user.role,
    }

