# /app/services/submission_service.py

from sqlalchemy.orm import Session
from app.models.submission_models import Submission
from app.models.repo_model import Repository
from app.models.evaluation_model import EvaluationCriterion
from app.schemas.submission_schema import SubmissionCreate
from app.models.user_model import User

import logging

logger = logging.getLogger(__name__)


def create_submission(
    db: Session,
    user: User,
    submission_data: SubmissionCreate
) -> Submission:
    try:
        logger.info(f"📝 제출 시도 by {user.email} - 팀명: {submission_data.team_name}, 대회: {submission_data.competition_name}")

        submission = Submission(
            user_id=user.id,
            team_name=submission_data.team_name,
            title=submission_data.title,
            description=submission_data.description,
            competition_name=submission_data.competition_name,
            status="submitted"
        )
        db.add(submission)
        db.flush()  # ID 할당

        for repo in submission_data.repositories:
            logger.debug(f"🔗 레포 추가: type={repo.type}, url={repo.repo_url}")
            db.add(Repository(
                submission_id=submission.id,
                type=repo.type,
                repo_url=repo.repo_url,
            ))

        for criterion in submission_data.evaluation_criteria:
            logger.debug(f"📋 평가 항목 추가: {criterion.name}")
            db.add(EvaluationCriterion(
                submission_id=submission.id,
                name=criterion.name
            ))

        db.commit()
        db.refresh(submission)

        logger.info(f"✅ 제출 완료 - 제출 ID: {submission.id}, 사용자: {user.email}")
        return submission

    except Exception as e:
        db.rollback()
        logger.exception(f"🔥 제출 실패 - 사용자: {user.email}, 에러: {str(e)}")
        raise
