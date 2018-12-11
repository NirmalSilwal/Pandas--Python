import pandas as pd
import numpy as np
df=pd.read_csv("temp.csv")
print (df)
print (df[['Name', 'City']])
print(df[df['City'] == 'Toronto'].head(1))
