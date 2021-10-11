import sqlalchemy as db
import sqlite3 as sql
from sqlalchemy import create_engine, Table, Column, MetaData
import pandas as pd
import numpy as np
import glob
import os


def main():
    
    # Option 1 to read from csv files 
    #folder_path = r'C:\Users\nurca\OneDrive\Desktop\Python test'
    #file_names = glob.glob(folder_path + "/*.csv")

    #li = []
    #for file_name in file_names:
    #    print(file_name)
    #    df = pd.read_csv(file_name, index_col=None, header=0)
    #    li.append(df)

    #frame = pd.concat(li, axis=0, ignore_index=True)
    #print(frame)
    

    # Option 2 to read from csv files
    df = pd.concat(map(pd.read_csv, glob.glob(os.path.join('',"*.csv"))), ignore_index=True)
    #print (df)

    #conn = sqlite3.connect('test.db')
    #print(conn)

    try:
        #engine = create_engine('sqlite:///nug.db', echo=True)
        conn = sql.connect('nug.db')
        df.to_sql('nug_table',conn)
    except:
        print("Failed to create engine.")

    cn = sql.connect('nug.db')
    nug_df = pd.read_sql('select * from nug_table where Y1="YYY1"', cn)
    print(nug_df)

    #SQLalchemy time
    #df.to_sql('nug_table', con=engine, index=True, index_label='id', if_exists='replace')

  
if __name__ == '__main__':
    main()