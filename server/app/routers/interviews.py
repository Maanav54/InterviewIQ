from fastapi import APIRouter
from ..schemas import QuestionRequest, EvaluationRequest
from ..services.ai import questions, evaluate
router=APIRouter(prefix="/interviews",tags=["Interviews"])
@router.post("/questions")
async def generate_questions(data:QuestionRequest): return {"questions":questions(data.role,data.difficulty,data.company,data.skills)}
@router.post("/evaluate")
async def evaluate_answer(data:EvaluationRequest): return evaluate(data.answer,data.topic)
