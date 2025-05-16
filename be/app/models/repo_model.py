# app/models/repo_model.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base


class Repository(Base):
    __tablename__ = "repositories"

    id = Column(Integer, primary_key=True, index=True)
    submission_id = Column(Integer, ForeignKey("submissions.id"))
    type = Column(String(50), nullable=False)  # ✅ 레포 타입 frontend, backend, fullstack 등
    repo_url = Column(String(500), nullable=False)  # ✅ URL 500글자 제한
    # 관계설정
    submission = relationship("Submission", back_populates="repositories")
