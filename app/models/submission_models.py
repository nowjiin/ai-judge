# app/models/submission_models.py

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy import Enum as SqlEnum
from sqlalchemy.orm import relationship
from datetime import datetime
from zoneinfo import ZoneInfo
from app.core.database import Base
import enum

KST = ZoneInfo("Asia/Seoul")


def now_kst():
    return datetime.now(KST)


class SubmissionStatus(str, enum.Enum):
    submitted = "submitted"
    grading = "grading"
    completed = "completed"
    failed = "failed"


class Submission(Base):
    __tablename__ = "submissions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))  # 로그인한 유저
    team_name = Column(String(100), nullable=False)
    title = Column(String(100), nullable=False)  # ✅ 최대 100자
    description = Column(String(1000), nullable=True)  # ✅ 최대 1000자
    submitted_at = Column(DateTime, default=now_kst)
    # ✅ 채점 상태
    status = Column(SqlEnum(SubmissionStatus), default=SubmissionStatus.submitted)
    # 관계설정
    repositories = relationship("Repository", back_populates="submission", cascade="all, delete")