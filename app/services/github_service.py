# app/services/github_service.py

# GitHub API를 사용하기 위한 라이브러리
from github import Github, GithubException

# 설정 값 (예: GITHUB_TOKEN) 불러오기
from app.core.config import settings

# 타입 힌팅용
from typing import Dict, List, Optional

# base64 디코딩용
import base64

# 정규 표현식 검사용
import re


# GitHub API를 통해 저장소 코드를 가져오는 서비스 클래스
class GitHubService:
    def __init__(self):
        # GITHUB_TOKEN이 있으면 인증된 요청 사용 (rate limit ↑)
        self.github = Github(settings.GITHUB_TOKEN) if settings.GITHUB_TOKEN else Github()

    def _extract_repo_info(self, repo_url: str) -> tuple[str, str]:
        """
        GitHub URL에서 owner와 repo 이름을 추출합니다.
        예: https://github.com/user/repo → ('user', 'repo')
        """
        parts = repo_url.strip('/').split('/')
        if len(parts) < 2:
            raise ValueError("Invalid GitHub repository URL")
        return parts[-2], parts[-1]

    def _should_ignore_file(self, path: str) -> bool:
        """특정 경로가 무시 대상인 파일/폴더인지 판단합니다."""

        # .git 디렉토리 무시
        if '.git/' in path:
            return True

        # 무시할 경로/확장자 패턴 정의 (정규표현식)
        ignore_patterns = [
            r'\.(git|DS_Store|pyc|pyo|pyd|so|dylib|dll|exe|bin|obj|o|a|lib|dylib|so|dll|exe|bin|obj|o|a|lib)$',
            r'node_modules/',
            r'venv/',
            r'__pycache__/',
            r'\.env',
            r'\.idea/',
            r'\.vscode/',
            r'\.pytest_cache/',
            r'\.coverage',
            r'\.tox/',
            r'dist/',
            r'build/',
            r'.*\.egg-info/',
        ]

        # 하나라도 패턴에 해당하면 True
        return any(re.search(pattern, path) for pattern in ignore_patterns)

    def _is_binary_file(self, content: str) -> bool:
        """해당 문자열이 바이너리 파일인지 확인 (디코딩 실패 여부 기준)"""
        try:
            content.encode('utf-8') # 다시 인코딩 시도
            return False
        except UnicodeEncodeError:
            return True

    def fetch_repository_files(self, repo_url: str) -> Dict[str, str]:
        """
        GitHub 저장소의 모든 코드 파일을 가져옵니다.
        반환 형식은 { 경로: 코드내용 }의 딕셔너리입니다.

        Args:
            repo_url (str): GitHub 저장소 URL

        Returns:
            Dict[str, str]: 파일 경로와 내용 딕셔너리

        Raises:
            ValueError: URL 파싱 실패, GitHub 접근 실패 등의 예외
        """
        try:
            # owner/repo 추출
            owner, repo_name = self._extract_repo_info(repo_url)

            # 저장소 객체 가져오기
            repo = self.github.get_repo(f"{owner}/{repo_name}")

            # 최종 반환 딕셔너리
            files = {}

            # 재귀적으로 폴더를 순회하며 파일을 처리하는 내부 함수
            def process_contents(contents, current_path=""):
                for content in contents:
                    # 경로 재구성 (디렉토리 내라면 full path)
                    path = f"{current_path}/{content.name}" if current_path else content.name

                    # 무시 대상이라면 skip
                    if self._should_ignore_file(path):
                        continue

                    # 파일 처리
                    if content.type == "file":
                        try:
                            # base64 디코딩
                            file_content = content.decoded_content.decode('utf-8')

                            # 바이너리 파일이라면 skip
                            if self._is_binary_file(file_content):
                                continue

                            # 최종 저장
                            files[path] = file_content

                        except (UnicodeDecodeError, GithubException) as e:
                            print(f"Error processing file {path}: {str(e)}")
                            continue

                    # 디렉토리면 재귀 호출
                    elif content.type == "dir":
                        try:
                            # 디렉토리 내용 가져오기
                            dir_contents = repo.get_contents(path)
                            process_contents(dir_contents, path)
                        except GithubException as e:
                            print(f"Error processing directory {path}: {str(e)}")
                            continue

            # 저장소 루트 디렉토리부터 시작
            root_contents = repo.get_contents("")
            process_contents(root_contents)

            return files

        # GitHub API 에러별 상세 처리
        except GithubException as e:
            if e.status == 404:
                raise ValueError(f"Repository not found: {repo_url}")
            elif e.status == 403:
                raise ValueError("Access denied. Please check your GitHub token permissions.")
            else:
                raise ValueError(f"GitHub API error: {str(e)}")

        # 기타 예외 (URL 문제 등)
        except Exception as e:
            raise ValueError(f"Error fetching repository: {str(e)}")


# 싱글톤 인스턴스 (전역에서 사용 가능)
github_service = GitHubService()
