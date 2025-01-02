from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models import User
from app.schemas import UserCreate, UserResponse
from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm
from app.auth import hash_password, create_access_token, verify_password

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
    
    hashed_password = hash_password(user.password)
    new_user = User(username=user.username, password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

@router.post("/token/", tags=["auth"])
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    db = SessionLocal()
    user = db.query(User).filter(User.username == form_data.username).first()

    if not user or not verify_password(form_data.password, user.password):
        raise HTTPException(status_code=401, detail="Usuário ou senha incorretos")

    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}