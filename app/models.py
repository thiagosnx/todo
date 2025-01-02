from sqlalchemy import Column, Integer, String, DateTime, Enum
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
import enum
from app.database import Base

class TaskState(enum.Enum):
    pendente = "pendente"
    andamento = "andamento"
    concluida = "concluida"

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    titulo = Column(String, nullable=False)
    descricao = Column(String, nullable=True)
    estado = Column(Enum(TaskState), nullable=False, default=TaskState.pendente)
    data_criacao = Column(DateTime(timezone=True), server_default=func.now())
    data_atualizacao = Column(DateTime(timezone=True), onupdate=func.now())

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
