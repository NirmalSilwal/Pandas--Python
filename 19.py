import pandas as pd
import numpy as np

ipl_data = {'Team': ['Riders', 'Riders', 'Devils', 'Devils', 'Kings',
         'kings', 'Kings', 'Kings', 'Riders', 'Royals', 'Royals', 'Riders'],
         'Rank': [1, 2, 2, 3, 3,4 ,1 ,1,2 , 4,1,2],
         'Year': [2014,2015,2014,2015,2014,2015,2016,2017,2016,2014,2015,2017],
         'Points':[876,789,863,673,741,812,756,788,694,701,804,690]}
df = pd.DataFrame(ipl_data)

grouped = df.groupby(['Team','Year'])

for name,group in grouped:
    print (name)
    print (group)


grouped = df.groupby('Year')


print(grouped.get_group(2014))

print(grouped['Points'].agg([np.sum, np.mean, np.std]))

grouped = df.groupby('Team')
score = lambda x: (x - x.mean()) / x.std()*10
print ('score',grouped.transform(score))
print (df.groupby('Team').filter(lambda x: len(x) >= 3))
