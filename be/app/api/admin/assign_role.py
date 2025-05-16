# app/api/admin/assign_role.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.user_model import User
from app.services.user_guard import get_current_user, require_role
from pydantic import BaseModel

router = APIRouter()


# 🔸 요청 바디 스키마 정의
class AssignRoleRequest(BaseModel):
    user_id: int
    role: str  # 예: "judge", "user", "admin" (필요 시 제한 가능)


@router.post("/assign-role")
def assign_role(
        request: AssignRoleRequest,
        db: Session = Depends(get_db),
        current_user: User = Depends(get_current_user)
):
    # 🔐 관리자 권한 확인
    require_role(current_user, ["admin"])

    target_user = db.query(User).filter(User.id == request.user_id).first()
    if not target_user:
        raise HTTPException(status_code=404, detail="User not found")

    # 유효한 역할만 허용할 수도 있음
    if request.role not in ["user", "judge", "admin"]:
        raise HTTPException(status_code=400, detail="Invalid role")

    # 역할 부여
    target_user.role = request.role
    db.commit()

    return {"message": f"User {target_user.username} is now '{target_user.role}'"}
