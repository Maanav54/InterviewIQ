from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import User
from ..schemas import Register, Login, Token
from ..auth import hash_password, verify_password, create_token
router=APIRouter(prefix="/auth",tags=["Authentication"])
@router.post("/register",response_model=Token,status_code=201)
def register(data:Register,db:Session=Depends(get_db)):
    if db.query(User).filter_by(email=data.email).first(): raise HTTPException(409,"Email already registered")
    u=User(**data.model_dump(exclude={"password"}),password_hash=hash_password(data.password));db.add(u);db.commit();db.refresh(u);return {"access_token":create_token(u.id)}
@router.post("/login",response_model=Token)
def login(data:Login,db:Session=Depends(get_db)):
    u=db.query(User).filter_by(email=data.email).first()
    if not u or not verify_password(data.password,u.password_hash): raise HTTPException(401,"Invalid email or password")
    return {"access_token":create_token(u.id)}
