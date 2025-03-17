from fastapi import FastAPI
from app.routers import load_departments

#Initialization of the app
app = FastAPI()

# Include the upload router
app.include_router(load_departments.router)
@app.get("/")
async def root():
    if file.content_type != "text/csv":
        raise HTTPException(status_code=400, detail="Invalid file type. Please upload a CSV file.")
    

