import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(8, 4),
index = pd.date_range('1/1/2010', periods=8),
columns = ['A', 'B', 'C', 'D'])
print(df)
print(df.rolling(window=3).mean())
print (df.expanding(min_periods=1).mean())
