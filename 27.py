import pandas as pd
import numpy as np
df=pd.read_csv("temp.csv")
print (df)

df=pd.read_csv("temp.csv",index_col=['S.No'])
print (df)
df = pd.read_csv("temp.csv", dtype={'Salary': np.float64})
print (df.dtypes)

df=pd.read_csv("temp.csv", names=['a', 'b', 'c','d','e'])
print (df)
