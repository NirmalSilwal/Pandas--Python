import pandas as pd
import numpy as np

#Create a Dictionary of series
d = {'Name':pd.Series(['Raja','Raju','Ricky','Shiv','Vishnu','Ramesh','Mahender',
   'Lious','Salman','SRK','VV','MM']),
   'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])}

#Create a DataFrame
df = pd.DataFrame(d)
print(df)
print(df.axes)

print('sum',df.sum())

print('sum of axis',df.sum(1))

print('mean',df.mean())

print('std',df.std())

print('count',df.count())

print('median',df.median())

print('cumsum',df.cumsum())

print('describe', df.describe())


##object − Summarizes String columns
##number − Summarizes Numeric columns
##all − Summarizes all columns together

print(df.describe(include=['object']))
