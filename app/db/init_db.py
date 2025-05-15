# /app/db/init_db.py

from app.core.database import Base, engine
# 모든 모델 import (안 하면 테이블 안 생김)
from app.models import user_model, submission_models, repo_model


def init_db():
    """
    SQLAlchemy 모델 기반으로 테이블을 생성합니다.
    """
    Base.metadata.create_all(bind=engine)
