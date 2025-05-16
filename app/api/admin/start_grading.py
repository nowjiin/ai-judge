# /app/api/admin/start_grading.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.submission_models import Submission, SubmissionStatus
from app.models.user_model import User
from app.services.user_guard import get_current_user, require_role
import logging

logger = logging.getLogger(__name__)

router = APIRouter()


@router.post("/admin/start-grade-one/{submission_id}", tags=["🔐Admin-Only🔐"])
def start_grading_one(
        submission_id: int,
        db: Session = Depends(get_db),
        current_user: User = Depends(get_current_user)
):
    """
    ✅ 수동 채점 요청: 채점 가능한 상태의 제출을 1건 처리
    """
    # 권한 확인
    require_role(current_user, ["admin"])

    # 제출 조회
    submission = db.query(Submission).filter(Submission.id == submission_id).first()
    if not submission:
        raise HTTPException(status_code=404, detail="Submission not found")

    if submission.status != SubmissionStatus.submitted:
        raise HTTPException(status_code=400, detail="Submission is not in 'submitted' state")

    # 채점 상태 변경
    submission.status = SubmissionStatus.grading
    db.commit()

    logger.info(f"🧪 채점 시작 - 제출 ID: {submission.id}, 팀: {submission.team_name}")

    # TODO: OpenAI 채점 로직 연결 예정

    return {"message": "Grading started", "submission_id": submission.id}
