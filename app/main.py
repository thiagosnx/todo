from fastapi import FastAPI
from app.database import Base, engine
from app.routes import routes

app = FastAPI()