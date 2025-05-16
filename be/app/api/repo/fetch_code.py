# app/api/repo/fetch_code.py

# FastAPI에서 라우터를 정의하기 위한 모듈
from fastapi import APIRouter, HTTPException

# GitHub 코드 가져오는 서비스 객체
from app.services.github_service import github_service

# 요청/응답 스키마 정의
from app.schemas.fetch_code_schema import FetchCodeRequest, FetchCodeResponse

# 라우터 객체 생성
router = APIRouter(
    responses={
        200: {"description": "Successfully fetched repository files"},
        400: {"description": "Invalid repository URL or access denied"},
        404: {"description": "Repository not found"},
        500: {"description": "Internal server error"}
    }
)


# POST 요청 핸들러 정의: /fetch-code/
# 요청 모델: FetchCodeRequest (repo_url 포함)
# 응답 모델: FetchCodeResponse (repo 이름, 파일 목록, 코드 내용 포함)
@router.post("/", response_model=FetchCodeResponse)
async def fetch_code(request: FetchCodeRequest):
    """
    GitHub 저장소의 코드 파일 목록과 내용을 가져옵니다.

    Args:
        request (FetchCodeRequest): repo_url (GitHub 저장소 주소)

    Returns:
        FetchCodeResponse: repo 이름, 파일 경로 리스트, 각 코드 내용
    """
    try:
        # 예: https://github.com/nowjiin/ai-judge → ['github.com', 'nowjiin', 'ai-judge']
        repo_parts = str(request.repo_url).strip('/').split('/')

        # 마지막 2개 항목 (owner/repo) 추출
        # 예: nowjiin/ai-judge
        repo_name = '/'.join(repo_parts[-2:])

        # GitHub API로 저장소의 파일들 가져오기
        # files: Dict[path -> content]
        files = github_service.fetch_repository_files(str(request.repo_url))

        # 응답 형태로 반환
        return FetchCodeResponse(
            repo=repo_name,
            files=list(files.keys()),  # 파일 경로 리스트
            code=files  # 코드 내용 (Dict[path] = content)
        )

    # GitHubService 내부에서 raise한 예외 처리 (예: 잘못된 URL 형식 등)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    # 알 수 없는 에러 → 500 Internal Server Error 반환
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")
