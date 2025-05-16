# /app/schemas/submission_schema.py

from pydantic import BaseModel, HttpUrl
from typing import List, Optional


class RepoCreate(BaseModel):
    type: str  # 예: frontend, backend 등 레포지토리 유형
    repo_url: HttpUrl  # GitHub 저장소 URL


class SubmissionCreate(BaseModel):
    team_name: str  # ✅ 팀 이름 (예: FastCoders)
    title: str  # ✅ 서비스 제목 (예: AI 자동 채점 플랫폼)
    description: Optional[str] = None  # ⛳️ 서비스 설명 (선택)
    competition_name: str = "default"  # ✅ 대회 이름 (기본: default → 일반제출)
    repositories: List[RepoCreate]  # ✅ 제출할 레포지토리 목록 (2개 이상 가능)
    evaluation_criteria: List[str]  # ✅ 심사 기준표
