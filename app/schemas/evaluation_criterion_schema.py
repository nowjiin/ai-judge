from pydantic import BaseModel
from typing import Optional


# ✅ 클라이언트가 제출할 때 사용하는 스키마
class EvaluationCriterionCreate(BaseModel):
    name: str  # 예: "구현 완성도", "아이디어 창의성"


# ✅ 평가된 항목을 반환할 때 사용하는 스키마
class EvaluationCriterionResponse(BaseModel):
    id: int
    name: str
    score: Optional[int] = None
    feedback: Optional[str] = None

    class Config:
        orm_mode = True