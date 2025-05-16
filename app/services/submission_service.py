# /app/services/submission_service.py (수정됨)

from sqlalchemy.orm import Session
from app.models.submission_models import Submission
from app.models.repo_model import Repository
from app.models.user_model import User
from app.models.evaluation_model import EvaluationCriterion
from app.schemas.submission_schema import SubmissionCreate
from app.services.github_service import github_service
from app.services.repo_snapshot_service import save_repo_snapshots
import logging

logger = logging.getLogger(__name__)


def create_submission(
    db: Session,
    user: User,
    submission_data: SubmissionCreate
) -> Submission:
    try:
        logger.info(f"📍 Submission from {user.email} | 💼 Team: {submission_data.team_name}")

        # 1. Submission 객체 생성 및 추가
        submission = Submission(
            user_id=user.id,
            team_name=submission_data.team_name,
            title=submission_data.title,
            description=submission_data.description,
            competition_name=submission_data.competition_name,
            status="submitted"
        )
        db.add(submission)
        db.flush()  # ID를 받아오기 위해 flush

        # 2. 연결된 Repository 정보 저장
        for repo in submission_data.repositories:
            db.add(Repository(
                submission_id=submission.id,
                type=repo.type,
                repo_url=repo.repo_url
            ))

        # 3. 평가 기준 항목 저장
        for criterion_name in submission_data.evaluation_criteria:
            db.add(EvaluationCriterion(
                submission_id=submission.id,
                name=criterion_name
            ))

        db.commit()
        db.refresh(submission)

        # ✅ 제출된 레포들 GitHub에서 코드 fetch 후 snapshot 저장
        for repo in submission.repositories:
            try:
                files = github_service.fetch_repository_files(repo.repo_url)
                save_repo_snapshots(db, submission.id, repo.repo_url, files)
            except Exception as e:
                logger.warning(f"⚠️ Snapshot 저장 실패 - repo: {repo.repo_url}, 에러: {e}")

        logger.info(f"✅ Submitted successfully ID={submission.id}")
        return submission
    except Exception as e:
        db.rollback()
        logger.exception("❌ Submission failed")
        raise


def fetch_submission_data(db: Session):
    try:
        submissions = db.query(Submission).all()
        logger.info(f"📁 Retrieved {len(submissions)} submissions")
        return [
            {
                "submission_id": s.id,
                "team_name": s.team_name,
                "title": s.title,
                "description": s.description,
                "competition_name": s.competition_name,
                "submitted_at": s.submitted_at,
                "status": s.status,
                "user_id": s.user_id,
                "repositories": [
                    {"type": r.type, "repo_url": r.repo_url}
                    for r in s.repositories
                ],
                "evaluation_criteria": [c.criterion for c in s.evaluation_criteria]
            }
            for s in submissions
        ]
    except Exception as e:
        logger.exception("❌ Failed to fetch submissions")
        raise
