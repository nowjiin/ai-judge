# app/models/fetch_code_models.py

from pydantic import BaseModel
from typing import Dict

class FetchCodeRequest(BaseModel):
    repo_url: str

class FetchCodeResponse(BaseModel):
    repo: str
    files: Dict[str, str]  # {파일 경로: 코드 내용}
