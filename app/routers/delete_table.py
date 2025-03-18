import pandas as pd
from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy import select,MetaData,Table
from typing import List
from app.database import SessionLocal,get_db
from app import models


router = APIRouter(prefix="/delete_table", tags=["Delete table"])
@router.delete("/{tablename}")
def delete_table(tablename:str, db: Session = Depends(get_db)):
    metadata = MetaData()
    try:
        # Reflect the table based on the table name provided
        table = Table(tablename, metadata, autoload_with=db.bind)
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Table '{tablename}' not found.")

    results = db.execute(table.delete())
    db.commit()
    