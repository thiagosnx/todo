from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from app.database import Base, engine
from app.routes import auth, tasks

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(auth.router)
app.include_router(tasks.router)