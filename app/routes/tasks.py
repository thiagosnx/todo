from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from app.database import SessionLocal
from app.models import Task, TaskState
from app.schemas import TaskCreate, TaskResponse

router = APIRouter(
    prefix="/tasks",
    tags=["tasks"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=List[TaskResponse])
def read_tasks(db: Session = Depends(get_db)):
    return db.query(Task).all()