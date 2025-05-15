# app/services/submission_service.py

from sqlalchemy.orm import Session
from app.models.submission_models import Submission
from app.models.repo_model import Repository
from app.schemas.submission_schema import SubmissionCreate
from app.models.user_model import User


def create_submission(
    db: Session,
    user: User,
    submission_data: SubmissionCreate
) -> Submission:
    submission = Submission(
        user_id=user.id,
        team_name=submission_data.team_name,
        title=submission_data.title,
        description=submission_data.description,
    )
    db.add(submission)
    db.flush()  # ID 할당을 위해 flush()

    for repo in submission_data.repositories:
        db.add(Repository(
            submission_id=submission.id,
            type=repo.type,
            repo_url=repo.repo_url,
        ))

    db.commit()
    db.refresh(submission)
    return submission


def fetch_submission_data(db: Session):
    submissions = db.query(Submission).all()

    return [
        {
            "submission_id": s.id,
            "team_name": s.team_name,
            "title": s.title,
            "description": s.description,
            "submitted_at": s.submitted_at,
            "status": s.status,
            "user_id": s.user_id,
            "repositories": [
                {"type": r.type, "repo_url": r.repo_url}
                for r in s.repositories
            ]
        }
        for s in submissions
    ]
