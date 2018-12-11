import numpy as np
import pandas as pd

d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
      'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)
print(df ['one'])



df['three']=pd.Series([10,20,30],index=['a','b','c'])
print(df)


df['four']=df['one']+df['three']

print(df)

del df['one']
print(df)
