from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.utils import load_data,get_data_from_blob

router = APIRouter(prefix="/load_table", tags=["Load table"])

#Local Testing
#--------------------------------------------------------------------
#@router.post("/{tablename}")
#def load_table(tablename: str,db: Session = Depends(get_db)):
#    load_data(tablename,get_data(tablename))
#--------------------------------------------------------------------

@router.post("/{tablename}")
def load_table(tablename: str,db: Session = Depends(get_db)):
    load_data(tablename,get_data_from_blob(tablename))
    return {"message": "CSV file processed and data loaded into the database."}
