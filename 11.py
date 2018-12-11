import pandas as pd
import numpy as np

unsorted_df=pd.DataFrame(np.random.randn(10,2),index=[1,4,6,2,3,5,9,8,0,7],columns=['col2','col1'])
print(unsorted_df)

sorted_df=unsorted_df.sort_index(ascending=False)
print (sorted_df)

sorted_df=unsorted_df.sort_index(axis=1)
print (sorted_df)

sorted_df = unsorted_df.sort_values(by='col1')
print (sorted_df)

sorted_df = unsorted_df.sort_values(by=['col1','col2'])
print (sorted_df)
