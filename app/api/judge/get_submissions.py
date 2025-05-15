from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.submission_models import Submission
from app.models.user_model import User
from app.services.user_guard import get_current_user, require_role
# 서비스 로직
from app.services.submission_service import fetch_submission_data

router = APIRouter()


@router.get("/judge/submissions", tags=["judge"])
def get_all_submissions_judge(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    require_role(current_user, ["admin", "judge"])
    return fetch_submission_data(db)
