# GitHub API를 사용하기 위한 라이브러리
from github import Github, GithubException

# 설정값 로딩 (예: GITHUB_TOKEN)
from app.core.config import settings

# 타입 힌팅
from typing import Dict

# 정규 표현식
import re

# 로깅 설정
import logging

logger = logging.getLogger(__name__)


# GitHub 저장소로부터 코드 파일을 수집하는 서비스 클래스
class GitHubService:
    def __init__(self):
        # 인증 토큰이 설정되어 있으면 인증된 GitHub API 사용
        if settings.GITHUB_TOKEN:
            logger.info("🔐 인증된 GitHub API 사용 설정됨")
            self.github = Github(settings.GITHUB_TOKEN)
        else:
            logger.warning("⚠️ GitHub Token 미설정 - 비인증 API 사용 (Rate Limit 낮음)")
            self.github = Github()

    @staticmethod
    def _extract_repo_info(repo_url: str) -> tuple[str, str]:
        """
        GitHub URL에서 저장소 소유자(owner)와 저장소 이름(repo)을 추출합니다.
        예: 'https://github.com/user/repo' → ('user', 'repo')
        """
        parts = repo_url.strip('/').split('/')
        if len(parts) < 2:
            raise ValueError("Invalid GitHub repository URL")
        return parts[-2], parts[-1]

    @staticmethod
    def _should_ignore_file(path: str) -> bool:
        """
        무시해야 할 파일 또는 디렉토리인지 확인합니다.
        (예: 바이너리, 캐시 파일, 환경설정 파일 등)
        """
        ignore_patterns = [
            r'\.(git|DS_Store|pyc|pyo|pyd|so|dylib|dll|exe|bin|obj|o|a|lib)$',
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
        return any(re.search(pattern, path) for pattern in ignore_patterns)

    @staticmethod
    def _is_binary_file(content: str) -> bool:
        """
        문자열이 바이너리 데이터인지 확인합니다.
        (UTF-8 인코딩 실패 여부를 통해 판단)
        """
        try:
            content.encode('utf-8')
            return False
        except UnicodeEncodeError:
            return True

    def fetch_repository_files(self, repo_url: str) -> Dict[str, str]:
        """
        주어진 GitHub 저장소에서 모든 코드 파일을 가져옵니다.
        무시 대상 파일 및 바이너리 파일은 제외합니다.

        Args:
            repo_url (str): GitHub 저장소 URL

        Returns:
            Dict[str, str]: { 파일 경로: 코드 내용 } 형태의 딕셔너리 반환

        Raises:
            ValueError: 유효하지 않은 URL이거나 API 오류 발생 시
        """
        logger.info(f"📥 GitHub 레포 fetch 시작: {repo_url}")
        try:
            # URL에서 owner와 repo 이름 추출
            owner, repo_name = self._extract_repo_info(repo_url)
            repo = self.github.get_repo(f"{owner}/{repo_name}")
            files = {}

            def process_contents(contents, current_path=""):
                for content in contents:
                    path = f"{current_path}/{content.name}" if current_path else content.name

                    # 무시 대상 파일/디렉토리는 스킵
                    if self._should_ignore_file(path):
                        logger.debug(f"🚫 무시된 파일: {path}")
                        continue

                    if content.type == "file":
                        try:
                            file_content = content.decoded_content.decode('utf-8')
                            if self._is_binary_file(file_content):
                                logger.debug(f"⚠️ 바이너리 파일 무시됨: {path}")
                                continue
                            files[path] = file_content
                            logger.debug(f"📄 파일 추가됨: {path}")
                        except (UnicodeDecodeError, GithubException) as e:
                            logger.warning(f"⚠️ 파일 처리 실패: {path} → {str(e)}")
                            continue

                    elif content.type == "dir":
                        try:
                            dir_contents = repo.get_contents(path)
                            process_contents(dir_contents, path)
                        except GithubException as e:
                            logger.warning(f"📁 디렉토리 접근 실패: {path} → {str(e)}")
                            continue

            # 루트 디렉토리부터 시작하여 재귀적으로 탐색
            root_contents = repo.get_contents("")
            process_contents(root_contents)

            logger.info(f"✅ 레포 fetch 완료: {repo_url} - 총 {len(files)}개 파일")
            return files

        except GithubException as e:
            logger.error(f"❌ GitHub API 오류 - {repo_url} → {str(e)}")
            if e.status == 404:
                raise ValueError(f"Repository not found: {repo_url}")
            elif e.status == 403:
                raise ValueError("Access denied. Please check your GitHub token permissions.")
            else:
                raise ValueError(f"GitHub API error: {str(e)}")

        except Exception as e:
            logger.exception(f"🔥 레포 fetch 중 예외 발생 - {repo_url}")
            raise ValueError(f"Error fetching repository: {str(e)}")


# 전역에서 사용할 수 있는 GitHubService 싱글톤 인스턴스
github_service = GitHubService()