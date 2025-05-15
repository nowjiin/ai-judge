# app/api/submission/create_submission.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.services.user_guard import get_current_user
from app.services.submission_service import create_submission
from app.schemas.submission_schema import SubmissionCreate
from app.models.user_model import User

router = APIRouter()


@router.post("/submit")
def submit_project(
    submission_data: SubmissionCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return create_submission(db, current_user, submission_data)