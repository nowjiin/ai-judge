# app/models/submission_models.py

from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean, Text
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
    # ✅ PK
    id = Column(Integer, primary_key=True, index=True)
    # ✅ user id
    user_id = Column(Integer, ForeignKey("users.id"))
    # ✅ 대회 여부 : 공백이면 일반 제출 / 대회면 대회 이름이 있음.
    competition_name = Column(String(100), nullable=False, default="")
    # ✅ 팀 이름 : 최대 100자
    team_name = Column(String(100), nullable=False)
    # ✅ 서비스 명 : 최대 100자
    title = Column(String(100), nullable=False)
    # ✅ 프로젝트 설명 : 최대 1000자
    description = Column(String(1000), nullable=True)
    # ✅ 제출 시간
    submitted_at = Column(DateTime, default=now_kst)
    # ✅ 채점 상태
    status = Column(SqlEnum(SubmissionStatus), default=SubmissionStatus.submitted)
    # ✅ 채점 점수결과
    score = Column(Integer, nullable=True)
    # ✅ GPT 채점 근거 / feedback
    feedback = Column(Text, nullable=True)  # GPT 요약
    # ✅ 피드백 사용자에게 공개 여부
    feedback_visible = Column(Boolean, default=False)
    # 관계설정
    repositories = relationship("Repository", back_populates="submission", cascade="all, delete")