from posixpath import dirname
import sqlalchemy as db
from sqlalchemy import create_engine
import sqlite3 as sql
import pandas as pd
import glob
import os

def add_record(db, data):
    #insert record into table
    with sql.connect(db) as conn:
        print("test")

def main():
    #print("test")
    
    try:
        engine = create_engine('sqlite:///nug.db', echo=False)
    except:
        print("Failed to create engine.")

    #print(glob.glob(os.path.join('',"file1.csv")))
    #pd.read_csv(glob.glob(os.path.join('',"file1.csv")))
    #print(os.getcwd())
    #pd.read_csv(os.path.join(os.path.dirname(__file__),"file1.csv"))
    #print("".join((os.getcwd(),"/file1.csv")))
    #csv_path = os.path.join(os.getcwd(),"file1.csv")
    #print(csv_path)
    #pd.read_csv("C:\Users\nurca\OneDrive\Desktop\Python test\file1.csv")
    df = pd.read_csv(os.path.join(os.getcwd(),"file1.csv"))
    print(df)
    df.to_sql('new_table',con=engine, index=False, if_exists='replace')
    #df.to_sql('new_table',con=engine, index=False, if_exists='append')

    #print(os.path.join(os.getcwd(),"file1.csv"))


if __name__ == "__main__":
    main()