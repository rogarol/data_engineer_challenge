import pandas as pd
from app.database import engine

def get_data(filename:str)->pd.DataFrame: 
    df = pd.read_csv(f'/Users/rodrigogarci/Downloads/data_challenge_files/{filename}.csv',header=None)
    return df

def load_data(tablename:str,df:pd.DataFrame)->None:
    df.to_sql(tablename, con=engine, if_exists="replace", index=False)
    return {"message": "CSV file processed and data loaded into SQLite database."}