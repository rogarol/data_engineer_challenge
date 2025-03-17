from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

#For local testing we work with SQLite, then we switch to Azure#
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

#Creation of the engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False},echo=True
)

#Creation of the session
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#Base class to define DB Objects
Base = declarative_base()