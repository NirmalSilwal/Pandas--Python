import pandas as pd

pd.describe_option("display.max_rows")
print (' before max rows',pd.get_option("display.max_rows"))
print (' before max cols',pd.get_option("display.max_columns"))
pd.set_option("display.max_rows",80)
pd.set_option("display.max_columns",30)

print (' after max rows',pd.get_option("display.max_rows"))
print ('after max cols',pd.get_option("display.max_columns"))
pd.reset_option("display.max_rows")

print (' after reset max rows',pd.get_option("display.max_rows"))
print (' after reset max cols',pd.get_option("display.max_columns"))
