# /app/models/evaluation_model.py

from sqlalchemy import Column, Integer, String, ForeignKey, Text
from sqlalchemy.orm import relationship
from app.core.database import Base


class EvaluationCriterion(Base):
    __tablename__ = "evaluation_criteria"

    id = Column(Integer, primary_key=True, index=True)
    submission_id = Column(Integer, ForeignKey("submissions.id", ondelete="CASCADE"), nullable=False)

    # ✅ 항목 이름 (예: 코드 품질, 구조, 창의성 등)
    name = Column(String(100), nullable=False)

    # ✅ 평가 점수 (OpenAI가 채점한 숫자 등)
    score = Column(Integer, nullable=True)

    # ✅ 항목별 GPT 피드백
    feedback = Column(Text, nullable=True)

    # 관계 (선택: submission 객체에서 criteria 리스트로 접근 가능하게)
    submission = relationship("Submission", back_populates="criteria")
