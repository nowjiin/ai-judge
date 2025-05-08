from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, HttpUrl
from typing import Dict
from app.services.github_service import github_service

router = APIRouter(
    prefix="/fetch-code",
    tags=["fetch-code"],
    responses={
        200: {"description": "Successfully fetched repository files"},
        400: {"description": "Invalid repository URL or access denied"},
        404: {"description": "Repository not found"},
        500: {"description": "Internal server error"}
    }
)

class FetchCodeRequest(BaseModel):
    repo_url: HttpUrl

class FetchCodeResponse(BaseModel):
    repo: str
    files: Dict[str, str]

@router.post("/", response_model=FetchCodeResponse)
async def fetch_code(request: FetchCodeRequest):
    """
    GitHub 저장소의 코드를 가져옵니다.
    
    Args:
        request: GitHub 저장소 URL을 포함한 요청 객체
        
    Returns:
        FetchCodeResponse: 저장소 이름과 파일 내용을 포함한 응답 객체
        
    Raises:
        HTTPException: 저장소 접근 실패 또는 내부 오류 발생 시
    """
    try:
        # 저장소 URL에서 owner/repo 형식 추출
        repo_parts = str(request.repo_url).strip('/').split('/')
        repo_name = '/'.join(repo_parts[-2:])
        
        # 파일 가져오기
        files = github_service.fetch_repository_files(str(request.repo_url))
        
        return FetchCodeResponse(
            repo=repo_name,
            files=files
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}") 