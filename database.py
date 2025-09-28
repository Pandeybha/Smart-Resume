from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Apne PostgreSQL ka connection string
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:MyNewPassword123@localhost:5432/resume_db"


# Engine create karo
engine = create_engine(SQLALCHEMY_DATABASE_URL, future=True)

# Session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()

# Dependency function (FastAPI ke liye)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
