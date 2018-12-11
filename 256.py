import numpy as np
import pandas as pd

population_dict ={'California': 38332521,
'Texas': 26448193,
'New York': 19651127,
'Florida': 19552860,
'Illinois': 12882135}
population = pd.Series(population_dict)

data = pd.DataFrame(population, columns=['population'])

print(data)


lists = [{'a': i, 'b': 2 * i}
for i in range(3)]
data =pd.DataFrame(lists)
print(data)

missing = pd.DataFrame([{'a': 1, 'b': 2}, {'b': 3, 'c': 4}])
print(missing)

nparray =pd.DataFrame(np.random.rand(3, 2),
columns=['foo', 'bar'],
index=['a', 'b', 'c'])
print(nparray)
