from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy import MetaData,Table
from app.database import get_db


router = APIRouter(prefix="/delete_table", tags=["Delete table"])
@router.delete("/{tablename}")
def delete_table(tablename:str, db: Session = Depends(get_db)):
    metadata = MetaData()
    try:
        #Reflect the table based on the table name provided
        table = Table(tablename, metadata, autoload_with=db.bind)
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Table '{tablename}' not found.")

    db.execute(table.delete())
    db.commit()
    return {"message": "Table deleted successfully."}