##Indexing 	Description
##.loc() 	Label based
##.iloc() 	Integer based
##.ix() 	Both Label and Integer based

import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(8, 4),
index = ['a','b','c','d','e','f','g','h'], columns = ['A', 'B', 'C', 'D'])


print (df.loc[:,'A':'C'])
print (df.loc['a':'h'])
print (df.loc['c':'g','A':'C'])
print (df.loc[['a'],['A','C']])
print (df.loc['a']>0)
print (df.iloc[:4])
print (df.iloc[:4])
print (df.iloc[1:5, 2:4])
print (df.iloc[[1, 3, 5], [1, 3]])
print (df.ix[:4])
print (df.ix[:,'A'])

df = pd.DataFrame(np.random.randn(8, 4), columns = ['A', 'B', 'C', 'D'])
print (df['A'])
print (df[['A','B']])
print (df.D)


