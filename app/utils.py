import pandas as pd
from app.database import engine
from azure.storage.blob import BlobServiceClient
from os import getenv
from fastapi import HTTPException

def get_data(filename:str)->pd.DataFrame: 
    """This function is just for local testing"""
    df = pd.read_csv(f'/Users/rodrigogarci/Downloads/data_challenge_files/{filename}.csv',header=None)
    return df

def load_data(tablename:str,df:pd.DataFrame)->None:
    """This function is just for local testing"""
    df.to_sql(tablename, con=engine, if_exists="replace", index=False)
    return {"message": "CSV file processed and data loaded into SQLite database."}

def get_data_from_blob(blob_name: str) -> pd.DataFrame:
    sas_token = getenv('AZURE_SAS_TOKEN')
    account_url = getenv('AZURE_ACCOUNT_URL')
    container_name = getenv('AZURE_CONTAINER_NAME')
    blob_name = f'{blob_name}.csv'
    print(sas_token)
    print(account_url)
    print(container_name)
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
        print("OK")
        return df
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error reading blob: {e}")
