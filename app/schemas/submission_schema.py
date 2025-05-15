# app/schemas/submission_schema.py

from pydantic import BaseModel, HttpUrl
from typing import List, Optional


class RepoCreate(BaseModel):
    type: str
    repo_url: HttpUrl


class SubmissionCreate(BaseModel):
    team_name: str
    title: str
    description: Optional[str] = None
    repositories: List[RepoCreate]