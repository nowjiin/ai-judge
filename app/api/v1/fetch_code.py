# app/api/v1/fetch_code.py

from fastapi import APIRouter, HTTPException
from app.models.fetch_code_models import FetchCodeRequest, FetchCodeResponse
from app.services.github_service import fetch_all_code_files

router = APIRouter(
    prefix="/api/v1/fetch-code",
    tags=["fetch-code"],  # 이름 설정
    responses={
        200: {"description": "Successful fetch"},
        404: {"description": "Repository not found"},
        500: {"description": "Internal Server Error"}
    }
)


@router.post("/", response_model=FetchCodeResponse)
async def fetch_code(request: FetchCodeRequest):
    try:
        files = fetch_all_code_files(request.repo_url)
        repo_name = '/'.join(request.repo_url.strip('/').split('/')[-2:])  # owner/repo 형태
        return FetchCodeResponse(repo=repo_name, files=files)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
