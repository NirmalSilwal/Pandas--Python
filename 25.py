import pandas as pd

print (pd.Timedelta('2 days 2 hours 15 minutes 30 seconds'))
print (pd.Timedelta(6,unit='h'))
print (pd.Timedelta(days=2))
s = pd.Series(pd.date_range('2012-1-1', periods=3, freq='D'))
td = pd.Series([ pd.Timedelta(days=i) for i in range(3) ])
df = pd.DataFrame(dict(A = s, B = td))
print (df)
df['C']=df['A']+df['B']

print (df)
