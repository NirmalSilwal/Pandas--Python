import pandas as pd
import numpy as np

#Create a Dictionary of series
d = {'Name':pd.Series(['Raja','Raju','Ricky','Shiv','Vishnu','Ramesh','Mahender',
   'Lious','Salman','SRK','VV','MM']),
   'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])}

#Create a DataFrame
df = pd.DataFrame(d)
##print(df)
##
##for col in df:
##   print(col)

   

##    iteritems() − to iterate over the (key,value) pairs
##
##    iterrows() − iterate over the rows as (index,series) pairs
##
##    itertuples() − iterate over the rows as namedtuples


##for key,value in df.iteritems():
##    print(key,value)

##for row_index,row in df.iterrows():
##   print (row_index,row)


for row in df.itertuples():
    print (row)
