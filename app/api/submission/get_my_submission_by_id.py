from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.services.user_guard import get_current_user
from app.models.user_model import User
from app.models.submission_models import Submission
from app.models.evaluation_model import EvaluationCriterion

router = APIRouter()


@router.get("/submissions/{submission_id}")
def get_my_submission_detail(
        submission_id: int,
        db: Session = Depends(get_db),
        current_user: User = Depends(get_current_user)
):
    # 제출물 가져오기
    submission = db.query(Submission).filter(Submission.id == submission_id).first()

    if not submission or submission.user_id != current_user.id:
        raise HTTPException(status_code=404, detail="제출 내역이 없거나 권한이 없습니다.")

    # 평가 항목 가져오기
    criteria = db.query(EvaluationCriterion).filter(EvaluationCriterion.submission_id == submission_id).all()

    return {
        "submission_id": submission.id,
        "team_name": submission.team_name,
        "title": submission.title,
        "description": submission.description,
        "competition_name": submission.competition_name,
        "submitted_at": submission.submitted_at,
        "status": submission.status,
        "score": submission.score,
        "feedback": submission.feedback if submission.feedback_visible else None,
        "repositories": [
            {"type": repo.type, "repo_url": repo.repo_url}
            for repo in submission.repositories
        ],
        "evaluation_criteria": [
            {"id": c.id, "name": c.name}
            for c in criteria
        ]
    }
