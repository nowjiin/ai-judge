# app/schemas/fetch_code_schema.py

# Pydantic의 BaseModel은 요청/응답 데이터의 검증과 자동 문서화를 위한 모델 베이스 클래스
from pydantic import BaseModel, HttpUrl
# 타입 힌팅용 모듈: List와 Dict 사용
from typing import List, Dict


# 🔹 요청 바디에 들어올 형식 정의
class FetchCodeRequest(BaseModel):
    # GitHub 저장소 주소 (URL 형식 검증 자동 지원)
    # 예: https://github.com/nowjiin/ai-judge
    repo_url: HttpUrl


# 🔹 응답 구조 정의
class FetchCodeResponse(BaseModel):
    # 저장소 이름 (owner/repo 형식 문자열)
    # 예: nowjiin/ai-judge
    repo: str

    # 파일 경로 리스트 (모든 파일 이름만 따로 추출)
    # 예: ["main.py", "utils/parser.py"]
    files: List[str]

    # 실제 코드 내용 (경로 → 코드 문자열 형태의 딕셔너리)
    # 예: { "main.py": "print('hello')", ... }
    code: Dict[str, str]
