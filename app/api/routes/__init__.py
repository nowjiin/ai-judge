# /app/api/routes/__init__.py

from fastapi import APIRouter
from app.api.auth import auth_router, check_role
from app.api.repo import fetch_code

# 사용자용
from app.api.submission import create_submission
from app.api.submission import get_my_submission
# 관리자(개발자용)
from app.api.admin import assign_role, get_submission
# Judge 용
from app.api.judge import get_submissions

router = APIRouter()

# 🧑‍💻===== 일반 사용자용 라우터 =====🧑‍💻
# submission 라우터 (레포 주소 제출, 팀명, 등등)
router.include_router(get_my_submission.router, tags=["submission"])  # 토큰으로 내가 제출한 내용 조회
router.include_router(create_submission.router, prefix="/submission", tags=["submission"])  # 토큰으로 제출
router.include_router(auth_router.router, prefix="/auth", tags=["auth"])  # 회원가입, 로그인
router.include_router(check_role.router, prefix="/auth", tags=["role-check"])  # ✅ 역할 확인 등 권한 API
router.include_router(fetch_code.router, prefix="/fetch-code", tags=["fetch"])  # 🧠 GitHub 코드 평가 fetch

# 🔐===== Admin 개발자용 라우터 =====🔐
# 심사위원 role 부여
router.include_router(assign_role.router, prefix="/admin", tags=["🔐Admin-Only🔐"])
router.include_router(get_submission.router, prefix="/admin", tags=["🔐Admin-Only🔐"])

# 🔐===== Judge용 라우터 =====🔐
router.include_router(get_submissions.router, tags=["judge"])
