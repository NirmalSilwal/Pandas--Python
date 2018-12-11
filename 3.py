import numpy as np
import pandas as pd

ind = pd.Index([2, 3, 5, 7, 11])
print(ind)
#Indexes are immutable
#ind[1] = 99

indA = pd.Index([1, 3, 5, 7, 9])
indB = pd.Index([2, 3, 5, 7, 11])
print(indA & indB) # intersection
print(indA | indB) # union
