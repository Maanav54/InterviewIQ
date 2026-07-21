from io import BytesIO
from fastapi import APIRouter, File, HTTPException, UploadFile
from pypdf import PdfReader

router = APIRouter(prefix="/resumes", tags=["Resume analysis"])
SKILL_KEYWORDS = {
    "React": ["react", "react.js", "reactjs"], "JavaScript": ["javascript", "typescript"],
    "Python": ["python"], "SQL": ["sql", "mysql", "postgresql"], "Git": ["git", "github"],
    "Docker": ["docker"], "Node.js": ["node.js", "nodejs"], "AWS": ["aws", "amazon web services"],
    "Machine Learning": ["machine learning", "tensorflow", "pytorch"], "Java": ["java"],
}

@router.post("/analyze")
async def analyze_resume(file: UploadFile = File(...)):
    if file.content_type != "application/pdf":
        raise HTTPException(400, "Please upload a PDF resume.")
    content = await file.read()
    if len(content) > 10 * 1024 * 1024:
        raise HTTPException(413, "Resume must be 10 MB or smaller.")
    try:
        text = " ".join(page.extract_text() or "" for page in PdfReader(BytesIO(content)).pages).lower()
    except Exception as exc:
        raise HTTPException(400, "This PDF could not be read.") from exc
    detected = [name for name, terms in SKILL_KEYWORDS.items() if any(term in text for term in terms)]
    missing = [skill for skill in ["Docker", "Unit testing", "System design", "CI/CD"] if skill.lower() not in text]
    score = min(96, 48 + len(detected) * 7 + (8 if "project" in text else 0) + (7 if "experience" in text else 0))
    return {"filename": file.filename, "ats_score": score, "skills": detected or ["No skills detected"], "missing_keywords": missing}
