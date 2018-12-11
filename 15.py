import pandas as pd
import numpy as np
s = pd.Series([1,2,3,4,5,4])
print (s.pct_change())
df = pd.DataFrame(np.random.randn(5, 2))
print(df)
print (df.pct_change())
print (df.pct_change(axis=1))

s1 = pd.Series(np.random.randn(10))
s2 = pd.Series(np.random.randn(10))
print (s1.cov(s2))
frame = pd.DataFrame(np.random.randn(10, 5), columns=['a', 'b', 'c', 'd', 'e'])
print (frame['a'].cov(frame['b']))
print (frame.cov())
print (frame['a'].corr(frame['b']))
print (frame.corr())
