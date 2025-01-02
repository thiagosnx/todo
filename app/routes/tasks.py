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

@router.get("/{task_id}", response_model=TaskResponse)
def read_task_by_id(task_id:int, db:Session = Depends(get_db)):
    db_task = db.query(Task).filter(Task.id == task_id).first()
    if not db_task:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    return db_task

@router.post("/", response_model=TaskResponse, status_code=201)
def create_task(task: TaskCreate, db:Session = Depends(get_db)):
    new_task = Task(titulo=task.titulo, descricao=task.descricao, estado=task.estado)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

@router.put("/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, task: TaskCreate, db: Session = Depends(get_db)):
    db_task = db.query(Task).filter(Task.id == task_id).first()
    if not db_task:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    
    db_task.titulo = task.titulo
    db_task.descricao = task.descricao
    db_task.estado = task.estado
    db.commit()
    db.refresh(db_task)
    return db_task

@router.delete("/{task_id}", status_code=204)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    db_task = db.query(Task).filter(Task.id == task_id).first()
    if not db_task:
        raise HTTPException(status_code=404, detail="Tarefa não encontrada")
    
    db.delete(db_task)
    db.commit()
    return {"message": "Tarefa excluída com sucesso"}


