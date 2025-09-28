from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas, crud, database

app = FastAPI()

# Root endpoint
@app.get("/")
def home():
    return {"message": "FastAPI Resume API is running 🚀"}

# ✅ Create resume
@app.post("/resumes/", response_model=schemas.ResumeOut)
def create_resume(resume: schemas.ResumeCreate, db: Session = Depends(database.get_db)):
    return crud.create_resume(db=db, resume=resume)

# ✅ Read all resumes
@app.get("/resumes/", response_model=list[schemas.ResumeOut])
def read_resumes(skip: int = 0, limit: int = 50, db: Session = Depends(database.get_db)):
    return crud.get_resumes(db, skip=skip, limit=limit)

# ✅ Read single resume
@app.get("/resumes/{resume_id}", response_model=schemas.ResumeOut)
def read_resume(resume_id: int, db: Session = Depends(database.get_db)):
    db_resume = crud.get_resume_by_id(db, resume_id)
    if not db_resume:
        raise HTTPException(status_code=404, detail="Resume not found")
    return db_resume

# ✅ Update resume
@app.put("/resumes/{resume_id}", response_model=schemas.ResumeOut)
def update_resume(resume_id: int, resume: schemas.ResumeCreate, db: Session = Depends(database.get_db)):
    db_resume = crud.update_resume(db, resume_id, resume)
    if not db_resume:
        raise HTTPException(status_code=404, detail="Resume not found")
    return db_resume

# ✅ Delete resume
@app.delete("/resumes/{resume_id}")
def delete_resume(resume_id: int, db: Session = Depends(database.get_db)):
    db_resume = crud.delete_resume(db, resume_id)
    if not db_resume:
        raise HTTPException(status_code=404, detail="Resume not found")
    return {"message": "Resume deleted successfully"}
