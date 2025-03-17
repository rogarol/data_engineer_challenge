import pandas as pd
from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from app.database import SessionLocal,get_db
from app import models

router = APIRouter(prefix="/load_departments", tags=["Load Departments"])

