from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session
from sqlalchemy import text
from app.database import get_db
from app.utils import generate_query
import io
import pandas as pd
from app.database import engine

router = APIRouter(prefix="/reports", tags=["Reports Endpoint"])
@router.get("/{report_number}")
def report_builder(report_number, db: Session = Depends(get_db)):
    try:
            sql_query = generate_query(report_number)
            df = pd.read_sql(sql_query, engine)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching data: {e}")

    # Write the DataFrame to an Excel file in memory
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df.to_excel(writer, index=False, sheet_name='Report_1')
    
    output.seek(0)
    headers = {"Content-Disposition": f'attachment; filename="Report_{report_number}.xlsx"'}
    return StreamingResponse(
            output,
            media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            headers=headers
        )





#try:
#        sql = text(generate_query(report_number))
#        result = db.execute(sql).fetchall()
#        report = [
#            {column: value for column, value in zip(result.keys(), row)}
#            for row in result
#        ]
#        return {"Report": report}
#    except Exception as e:
#        raise HTTPException(status_code=500, detail=str(e))