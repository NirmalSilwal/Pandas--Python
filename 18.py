import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(5, 3), index=['a', 'c', 'e', 'f',
'h'],columns=['one', 'two', 'three'])

df = df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])

print (df)

print (df['one'].isnull())
print (df['one'].notnull())
print (df['one'].sum())

df = pd.DataFrame(index=[0,1,2,3,4,5],columns=['one','two'])
print (df)
print (df['one'].sum())

print ("NaN replaced with '0':")
print (df.fillna(0))

df = pd.DataFrame(np.random.randn(5, 3), index=['a', 'c', 'e', 'f',
'h'],columns=['one', 'two', 'three'])
df = df.reindex(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])
print(df)
print (df.fillna(method='pad'))
print (df.fillna(method='backfill'))
print (df.dropna())
