import logging
from sqlalchemy.orm import Session
from app.models.repo_snapshot_models import RepositorySnapshot

logger = logging.getLogger(__name__)


def save_repo_snapshots(
    db: Session,
    submission_id: int,
    repo_url: str,
    files: dict[str, str]  # {file_path: file_content}
):
    """
    GitHub 레포의 파일 스냅샷을 DB에 저장합니다.
    """
    try:
        for path, content in files.items():
            snapshot = RepositorySnapshot(
                submission_id=submission_id,
                repo_url=repo_url,
                file_path=path,
                file_content=content
            )
            db.add(snapshot)
        db.commit()
        logger.info(f"✅ Repository snapshot 저장 완료 - 제출 ID: {submission_id}, 파일 수: {len(files)}")

    except Exception as e:
        db.rollback()
        logger.exception(f"❌ Repository snapshot 저장 실패 - 제출 ID: {submission_id}, 에러: {str(e)}")
        raise
