from pydantic import BaseModel, EmailStr, Field
class Register(BaseModel):
    name: str = Field(min_length=2); email: EmailStr; password: str = Field(min_length=8); college: str|None=None; branch: str|None=None; graduation_year: int|None=None
class Login(BaseModel): email: EmailStr; password: str
class Token(BaseModel): access_token: str; token_type: str="bearer"
class QuestionRequest(BaseModel): role: str; difficulty: str="medium"; company: str="product"; skills: list[str]=[]
class EvaluationRequest(BaseModel): question: str; answer: str = Field(min_length=10); topic: str="general"
