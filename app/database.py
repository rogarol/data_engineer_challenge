from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from os import getenv


#For local testing we work with SQLite, then we switch to Azure#
#SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
#Creation of the engine
#engine = create_engine(
#    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False},echo=True
#)

#We retrieve the values of our environmet variables to form the connection to the DB
username = getenv("AZURE_MYSQL_USERNAME")
password = getenv("AZURE_MYSQL_PASSWORD")
host = getenv("AZURE_MYSQL_HOST")
database = getenv("AZURE_MYSQL_DATABASE")
ssl_ca_path = getenv("AZURE_MYSQL_CA_CERF_PATH")

#Construct the connection URL for SQLAlchemy with MySQL Connector/Python driver
connection_url = f"mysql+mysqlconnector://{username}:{password}@{host}/{database}"

#Create the SQLAlchemy engine with the SSL certificate for secure connection
engine = create_engine(
connection_url,
    connect_args={
        "ssl_ca": ssl_ca_path,
        "ssl_verify_cert": True,
    }
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