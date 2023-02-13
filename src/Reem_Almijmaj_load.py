# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import requests


#Open the csv file and read it through panda dataframe
csv_data = pd.read_csv('WA_Fn-UseC_-Telco-Customer-Churn.csv')
# select the rows that they are Seniors only 

Senior_row = csv_data.loc[csv_data['SeniorCitizen']== 1]
# Select subset of the wanted columns from my dataframe 
df_3 = Senior_row[['customerID','tenure','Churn']]
# convert panda dataframe into json file and organize it based on the records
js = df_3.to_json(orient = 'records')
# upload json file data into the firebase
requests.put('https://dsci551-a7a0e-default-rtdb.firebaseio.com/.json', js)


