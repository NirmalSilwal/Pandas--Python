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

df_reindexed = df.reindex(index=[1,0,5], columns=['Age', 'Name', 'Rating'])

#print(df_reindexed)

df1 = pd.DataFrame(np.random.randn(10,3),columns=['col1','col2','col3'])
df2 = pd.DataFrame(np.random.randn(7,3),columns=['col1','col2','col3'])

df1 = df1.reindex_like(df2)
#print(df1)


df1 = pd.DataFrame(np.random.randn(6,3),columns=['col1','col2','col3'])
df2 = pd.DataFrame(np.random.randn(2,3),columns=['col1','col2','col3'])

# Padding NAN's
##print(df2.reindex_like(df1))

# Now Fill the NAN's with preceding Values
##print ("Data Frame with Forward Fill:")
##print(df2.reindex_like(df1,method='ffill'))
##
##print ("Data Frame with Back Fill:")
##print(df2.reindex_like(df1,method='bfill'))
##
##
##print ("Data Frame with Forward Fill limiting to 1:")
##print (df2.reindex_like(df1,method='ffill',limit=1))
##
df1 = pd.DataFrame(np.random.randn(4,3),columns=['col1','col2','col3'])
print (df1)

print ("After renaming the rows and columns:")
print(df1.rename(columns={'col1' : 'c1', 'col2' : 'c2'},
index = {0 : 21, 1 : 22, 2 : 23}))
