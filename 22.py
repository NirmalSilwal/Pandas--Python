import pandas as pd
print (pd.datetime.now())
print (pd.Timestamp('2017-03-01'))
print (pd.Timestamp(1587687255,unit='s'))
print (pd.date_range("11:00", "13:30", freq="30min").time)
print (pd.date_range("11:00", "13:30", freq="H").time)
print (pd.to_datetime(pd.Series(['Jul 31, 2009','2010-01-10', None])))
