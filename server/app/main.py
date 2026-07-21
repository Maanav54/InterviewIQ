from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .config import settings
from .database import Base, engine
from .routers import auth, interviews, dashboard, resumes
Base.metadata.create_all(bind=engine)
app=FastAPI(title="InterviewIQ API",version="1.0.0",description="AI-powered interview preparation API")
app.add_middleware(CORSMiddleware,allow_origins=[settings.frontend_origin],allow_credentials=True,allow_methods=["*"],allow_headers=["*"])
app.include_router(auth.router); app.include_router(interviews.router); app.include_router(dashboard.router)
app.include_router(resumes.router)
@app.get("/health",tags=["Health"])
async def health(): return {"status":"ok"}
