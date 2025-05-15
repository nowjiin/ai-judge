# app/models/fetch_code_models.py

# Pydantic: 데이터 유효성 검사 및 구조 정의를 위한 라이브러리
from pydantic import BaseModel

# Dict 타입 힌팅을 위한 모듈 (예: Dict[str, str])
from typing import Dict


# 🔹 클라이언트가 보내는 요청(request)의 구조를 정의
class FetchCodeRequest(BaseModel):
    # GitHub 저장소의 URL
    # 예: https://github.com/nowjiin/ai-judge
    repo_url: str


# 🔹 서버가 클라이언트에게 응답(response)할 구조 정의
class FetchCodeResponse(BaseModel):
    # 저장소 이름 (owner/repo 형식 문자열)
    # 예: nowjiin/ai-judge
    repo: str

    # 실제 코드 내용
    # 키: 파일 경로, 값: 해당 파일의 코드 내용
    # 예: { "main.py": "print('hello')", "utils/helper.py": "def helper(): ..." }
    files: Dict[str, str]
