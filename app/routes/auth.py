from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from app.database import SessionLocal
from app.models import User
from app.schemas import UserCreate, UserResponse
# from app.auth import hash_password

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/users/", response_model=UserResponse, tags=["auth"])
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    exists_user = db.query(User).filter(User.username == user.username).first()
    if exists_user:
        raise HTTPException(status_code=400, detail="Usuário já existe")
    
    hashed_password = user.password
    new_user = User(username=user.username, password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user