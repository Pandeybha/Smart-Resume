from sqlalchemy.orm import Session
from fastapi import HTTPException
from . import models, schemas

def create_resume(db: Session, resume: schemas.ResumeCreate):
    # Check if email already exists
    db_resume = db.query(models.Resume).filter(models.Resume.email == resume.email).first()
    if db_resume:
        raise HTTPException(status_code=400, detail="Email already registered")

    new_resume = models.Resume(name=resume.name, email=resume.email)
    db.add(new_resume)
    db.commit()
    db.refresh(new_resume)
    return new_resume

def get_resumes(db: Session, skip: int = 0, limit: int = 50):
    return db.query(models.Resume).offset(skip).limit(limit).all()

def get_resume_by_id(db: Session, resume_id: int):
    return db.query(models.Resume).filter(models.Resume.id == resume_id).first()

def update_resume(db: Session, resume_id: int, resume: schemas.ResumeCreate):
    db_resume = db.query(models.Resume).filter(models.Resume.id == resume_id).first()
    if not db_resume:
        raise HTTPException(status_code=404, detail="Resume not found")
    
    db_resume.name = resume.name
    db_resume.email = resume.email
    db.commit()
    db.refresh(db_resume)
    return db_resume

def delete_resume(db: Session, resume_id: int):
    db_resume = db.query(models.Resume).filter(models.Resume.id == resume_id).first()
    if not db_resume:
        raise HTTPException(status_code=404, detail="Resume not found")

    db.delete(db_resume)
    db.commit()
    return {"message": "Resume deleted successfully"}
