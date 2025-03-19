from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from sqlalchemy import text
from app.database import get_db
from ..utils import generate_query

router = APIRouter(prefix="/reports", tags=["Reports Endpoint"])
@router.get("/{report_number}")
def report_builder(report_number, db: Session = Depends(get_db)):
    try:
        sql = text(generate_query(report_number))
        result = Session.execute(sql)
        report = [dict(row) for row in result]
        return {"Report": report}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
