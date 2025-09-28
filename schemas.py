from pydantic import BaseModel, EmailStr

# Input schema (for creating / updating resume)
class ResumeCreate(BaseModel):
    name: str
    email: EmailStr


# Output schema (for responses)
class ResumeOut(BaseModel):
    id: int
    name: str
    email: EmailStr

    class Config:
        from_attributes = True   # Important for SQLAlchemy ORM
