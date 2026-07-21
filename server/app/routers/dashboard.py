from fastapi import APIRouter
router=APIRouter(prefix="/dashboard",tags=["Dashboard"])
@router.get("/summary")
async def summary(): return {"readiness":78,"interviews_completed":12,"average_score":73,"weak_topics":["DBMS","Computer Networks","Operating Systems"],"skill_scores":{"DSA":78,"DBMS":48,"OS":69,"React":88,"Python":82}}
