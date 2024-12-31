from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Use SQLite como banco de dados
DATABASE_URL = "sqlite:///./todo.db"  # Arquivo SQLite na raiz do projeto
# Para usar um banco em memória, substitua por: "sqlite:///:memory:"

# Configuração para SQLite
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
