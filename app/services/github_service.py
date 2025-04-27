# app/services/github_service.py

import requests
from urllib.parse import urlparse
import os
from dotenv import load_dotenv

load_dotenv()
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

HEADERS = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

def fetch_all_code_files(repo_url: str) -> dict:
    parsed = urlparse(repo_url)
    path_parts = parsed.path.strip('/').split('/')
    owner, repo = path_parts[0], path_parts[1]

    base_api_url = f"https://api.github.com/repos/{owner}/{repo}/contents"

    collected_files = {}

    def fetch_directory_contents(api_url):
        response = requests.get(api_url, headers=HEADERS)  # ✨ headers 추가
        response.raise_for_status()
        items = response.json()

        for item in items:
            if item['type'] == 'file' and item['name'].endswith(('.py', '.java', '.js', '.md', '.txt', '.yaml', '.yml')):
                file_content = requests.get(item['download_url'], headers=HEADERS).text
                collected_files[item['path']] = file_content
            elif item['type'] == 'dir':
                fetch_directory_contents(item['url'])

    fetch_directory_contents(base_api_url)

    return collected_files
