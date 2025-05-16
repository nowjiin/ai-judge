from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.services.user_guard import get_current_user
from app.models.user_model import User
from app.models.submission_models import Submission
from app.models.repo_model import Repository

router = APIRouter()


@router.get("/submissions/me")
def get_my_submission(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    submission = db.query(Submission).filter(Submission.user_id == current_user.id).first()
    if not submission:
        return {"message": "아직 제출한 프로젝트가 없습니다."}

    return {
        "submission_id": submission.id,
        "team_name": submission.team_name,
        "title": submission.title,
        "description": submission.description,
        "submitted_at": submission.submitted_at,
        "status": submission.status,
        "repositories": [
            {"type": repo.type, "repo_url": repo.repo_url}
            for repo in submission.repositories
        ]
    }