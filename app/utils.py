import pandas as pd
from app.database import engine
from azure.storage.blob import BlobServiceClient
from os import getenv
from fastapi import HTTPException

def evaluate_schema(tablename:str,df:pd.DataFrame)->None:
    """This function define the schema to rename the headers of the df in order to execute the df.to_sql command"""
    if tablename == "jobs":
        df.columns = ['id', 'job']
    elif tablename == "departments":
        df.columns = ['id', 'department']
    elif tablename == "employees":
        df.columns = ['id', 'name','datetime','department_id','job_id']
    
def get_data(filename:str)->pd.DataFrame: 
    """This function is just for local testing"""
    df = pd.read_csv(f'/Users/rodrigogarci/Downloads/data_challenge_files/{filename}.csv',header=None)
    evaluate_schema(filename,df)
    return df

def load_data(tablename:str,df:pd.DataFrame)->None:
    df.to_sql(tablename, con=engine, if_exists="append", index=False)
    

def get_data_from_blob(filename: str) -> pd.DataFrame:
    """This function allow to retrieve the information of the CSV files loaded on Azure Blob Storage Service"""
    sas_token = getenv('AZURE_SAS_TOKEN')
    account_url = getenv('AZURE_ACCOUNT_URL')
    container_name = getenv('AZURE_CONTAINER_NAME')
    blob_name = f'{filename}.csv'
    if not all([sas_token, account_url, container_name]):
        raise HTTPException(status_code=500, detail="Storage configuration is missing.")
    
    blob_client = BlobServiceClient(
        account_url=account_url,
        container_name=container_name,
        blob_name=blob_name,
        credential=sas_token
    )
    
    # Construct the full URL with the SAS token
    blob_url = f"{account_url}/{container_name}/{blob_name}?{sas_token}"

    try:
        df = pd.read_csv(blob_url,header=None)
        evaluate_schema(filename,df)
        print("OK")
        return df
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error reading blob: {e}")
