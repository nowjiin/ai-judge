from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from zoneinfo import ZoneInfo
from app.core.database import Base

KST = ZoneInfo("Asia/Seoul")


def now_kst():
    return datetime.now(KST)


class RepositorySnapshot(Base):
    __tablename__ = "repository_snapshots"

    id = Column(Integer, primary_key=True, index=True)
    submission_id = Column(Integer, ForeignKey("submissions.id"), nullable=False)
    repo_url = Column(String(300), nullable=False)
    file_path = Column(String(300), nullable=False)
    file_content = Column(Text, nullable=False)
    created_at = Column(DateTime, default=now_kst, nullable=False)

    # 관계설정
    submission = relationship("Submission", back_populates="repository_snapshots")