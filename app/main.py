from fastapi import FastAPI
from app.routers import load_table,read_table,delete_table
from app.database import Base,engine

# Create all tables on startup (for local dev)
Base.metadata.create_all(bind=engine)

#Initialization of the app
app = FastAPI()

# Include the upload router
app.include_router(load_table.router)

# Include the upload router
app.include_router(read_table.router)

# Include the delete router
app.include_router(delete_table.router)
