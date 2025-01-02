from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from app.database import SessionLocal
from app.models import Task, TaskState
from app.schemas import TaskCreate, TaskResponse