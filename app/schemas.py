from pydantic import BaseModel
from enum import Enum
from typing import Optional
from datetime import datetime

class TaskState(str, Enum):
    pendente = "pendente"
    andamento = "andamento"
    concluida = "concluida"

class TaskBase(BaseModel):
    titulo: str
    descricao: Optional[str] = None
    estado: TaskState

class TaskCreate(TaskBase):
    pass

class TaskResponse(TaskBase):
    id: int
    data_criacao: datetime
    data_atualizacao: Optional[datetime] = None

    class Config:
        from_attributes = True

class UserCreate(BaseModel):
    username:str
    password:str

class UserResponse(BaseModel):
    id: int
    username: str

    class Config: 
        from_attributes = True