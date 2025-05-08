# app/services/github_service.py

from github import Github, GithubException
from app.core.config import settings
from typing import Dict, List, Optional
import base64
from pathlib import Path
import re

class GitHubService:
    def __init__(self):
        self.github = Github(settings.GITHUB_TOKEN) if settings.GITHUB_TOKEN else Github()
    
    def _extract_repo_info(self, repo_url: str) -> tuple[str, str]:
        """GitHub URL에서 owner와 repo 이름을 추출합니다."""
        parts = repo_url.strip('/').split('/')
        if len(parts) < 2:
            raise ValueError("Invalid GitHub repository URL")
        return parts[-2], parts[-1]
    
    def _should_ignore_file(self, path: str) -> bool:
        """파일이 무시해야 할 파일인지 확인합니다."""
        # .git 디렉토리 무시
        if '.git/' in path:
            return True
        
        # 일반적인 무시 패턴
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
            r'*.egg-info/',
        ]
        
        return any(re.search(pattern, path) for pattern in ignore_patterns)
    
    def _is_binary_file(self, content: str) -> bool:
        """파일이 바이너리 파일인지 확인합니다."""
        try:
            content.encode('utf-8')
            return False
        except UnicodeEncodeError:
            return True
    
    def fetch_repository_files(self, repo_url: str) -> Dict[str, str]:
        """
        GitHub 저장소의 모든 코드 파일을 가져옵니다.
        
        Args:
            repo_url: GitHub 저장소 URL
            
        Returns:
            Dict[str, str]: {파일 경로: 파일 내용} 형태의 딕셔너리
            
        Raises:
            ValueError: 잘못된 저장소 URL
            GithubException: GitHub API 오류
        """
        try:
            owner, repo_name = self._extract_repo_info(repo_url)
            repo = self.github.get_repo(f"{owner}/{repo_name}")
            
            files = {}
            
            def process_contents(contents, current_path=""):
                for content in contents:
                    path = f"{current_path}/{content.name}" if current_path else content.name
                    
                    if self._should_ignore_file(path):
                        continue
                    
                    if content.type == "file":
                        try:
                            # 파일 내용 가져오기
                            file_content = content.decoded_content.decode('utf-8')
                            
                            # 바이너리 파일 체크
                            if self._is_binary_file(file_content):
                                continue
                                
                            files[path] = file_content
                        except (UnicodeDecodeError, GithubException) as e:
                            print(f"Error processing file {path}: {str(e)}")
                            continue
                            
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
            
        except GithubException as e:
            if e.status == 404:
                raise ValueError(f"Repository not found: {repo_url}")
            elif e.status == 403:
                raise ValueError("Access denied. Please check your GitHub token permissions.")
            else:
                raise ValueError(f"GitHub API error: {str(e)}")
        except Exception as e:
            raise ValueError(f"Error fetching repository: {str(e)}")

# 싱글톤 인스턴스 생성
github_service = GitHubService()
