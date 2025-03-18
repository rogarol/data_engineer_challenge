import pandas as pd
from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List
from app.database import SessionLocal,get_db
from app import models
from app.utils import get_data,load_data

router = APIRouter(prefix="/load_table", tags=["Load table"])

@router.post("/{tablename}")
async def load_table(tablename: str,db: Session = Depends(get_db)):
    load_data(tablename,get_data(tablename))

