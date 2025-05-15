from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, HttpUrl
from typing import Optional
from app.models.participant import ProjectType
from app.services.github_service import github_service

router = APIRouter()

class ParticipantSubmission(BaseModel):
    github_url: HttpUrl
    project_type: ProjectType
    description: str

class ParticipantResponse(BaseModel):
    id: int
    github_url: str
    project_type: ProjectType
    description: str
    score: Optional[int] = None
    feedback: Optional[str] = None

@router.post("/submit", response_model=ParticipantResponse)
async def submit_project(submission: ParticipantSubmission):
    # GitHub 저장소 정보 가져오기
    repo_info = github_service.fetch_repository_files(str(submission.github_url))
    if not repo_info:
        raise HTTPException(status_code=400, detail="Invalid GitHub repository URL")
    
    # TODO: 데이터베이스에 저장하는 로직 구현
    # 임시 응답
    return ParticipantResponse(
        id=1,
        github_url=str(submission.github_url),
        project_type=submission.project_type,
        description=submission.description
    ) 