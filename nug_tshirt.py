import pandas as pd
import sqlalchemy as db
from sqlalchemy import create_engine
import sqlite3 as sql
from sklearn import linear_model
import os
import matplotlib.pyplot as plt
import numpy as np

def regression(test_data, reg):
    print("Predicted from {} is {}.".format(test_data, reg.predict(test_data)))

def main():
    #Error handling when creating the engine to SQLite
    try:
        engine = create_engine('sqlite:///nug.db', echo=False)
    except:
        print("Failed to create engine.")

    #Read data from csv file and store it to dataframe
    tshirt_df = pd.read_csv(os.path.join(os.getcwd(), "t-shirt.csv"))
    #Create new table in SQLite based on dataframe
    tshirt_df.to_sql('tshirt_table',con=engine, index=False, if_exists='replace')
    #print(tshirt_df.describe())
    #print(tshirt_df[['T-Shirt Price']])
    #print(tshirt_df[['T-Shirt Sold']])

    #plotting the training data
    #plt.scatter(tshirt_df.iloc[:,0], tshirt_df.iloc[:,1], color='blue')
    #plt.xlabel('T-Shirt Price')
    #plt.ylabel('T-Shirt Sold')
    #plt.show()

    #regress to train the data
    train_x = np.asanyarray(tshirt_df[['T-Shirt Price']])
    train_y = np.asanyarray(tshirt_df[['T-Shirt Sold']])
    global reg
    reg = linear_model.LinearRegression()
    reg.fit(train_x, train_y)

    coef = reg.coef_
    intercept = reg.intercept_

    print('Coefficient/slope: {}'.format(coef))
    print('Intercept: {}'.format(intercept))

    #plotting the training data with regression result
    plt.scatter(tshirt_df.iloc[:,0], tshirt_df.iloc[:,1], color='blue')
    plt.plot(train_x, coef * train_x + intercept, color='red')
    plt.xlabel('T-Shirt Price')
    plt.ylabel('T-Shirt Sold')
    plt.show()
    
    #regression to predict - best candidate for the function
    test_data = [[8]]
    #test_y = reg.predict(test_data)
    #print('Prediction with $8 : {}'.format(test_y))
    regression(test_data,reg)

if __name__ == "__main__":
    main()