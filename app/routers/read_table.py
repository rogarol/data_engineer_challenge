import pandas as pd
from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy import select,MetaData,Table
from typing import List
from app.database import SessionLocal,get_db
from app import models


router = APIRouter(prefix="/tables", tags=["Read table"])
@router.get("/{tablename}")
async def read_table(tablename:str, db: Session = Depends(get_db)):
    metadata = MetaData()
    try:
        # Reflect the table based on the table name provided
        table = Table(tablename, metadata, autoload_with=db.bind)
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Table '{tablename}' not found.")

    stmt = select(table)
    results = db.execute(stmt).fetchall()
    # Convert each row to a dictionary for a JSON serializable response
    return [dict(row._mapping) for row in results]