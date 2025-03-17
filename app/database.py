from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

#For local testing we work with SQLite, then we switch to Azure#
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

#Creation of the engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False},echo=True
)

#Creation of the session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#Base class to define DB Objects
Base = declarative_base()

#We define this function to create a DB Connection for each request instead of while the app is running.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()