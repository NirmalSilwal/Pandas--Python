##A panel is a 3D container of data. 
##
##The names for the 3 axes are intended to give some semantic meaning to describing operations involving panel data. They are −
##
##    items − axis 0, each item corresponds to a DataFrame contained inside.
##
##    major_axis − axis 1, it is the index (rows) of each of the DataFrames.
##
##    minor_axis − axis 2, it is the columns of each of the DataFrames.

import pandas as pd
import numpy as np

data = np.random.rand(2,4,5)
print(data)
p = pd.Panel(data)
print(p)
data = {'Item1' : pd.DataFrame(np.random.randn(4, 3)), 
        'Item2' : pd.DataFrame(np.random.randn(4, 2))}
p = pd.Panel(data)
print(p)
print(p['Item1'])
print(p.major_xs(1))
print(p.minor_xs(1))
