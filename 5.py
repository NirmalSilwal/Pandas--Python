##Series Basic Functionality
##S.No. 	Attribute or Method 	Description
##1 	axes 	Returns a list of the row axis labels.
##2 	dtype 	Returns the dtype of the object.
##3 	empty 	Returns True if series is empty.
##4 	ndim 	Returns the number of dimensions of the underlying data, by definition 1.
##5 	size 	Returns the number of elements in the underlying data.
##6 	values 	Returns the Series as ndarray.
##7 	head() 	Returns the first n rows.
##8 	tail() 	Returns the last n rows.


import pandas as pd
import numpy as np


s = pd.Series(np.random.randn(4))
print(s)
print(s.axes)
print(s.empty)
print("The dimensions of the object:")
print(s.ndim)
print ("The size of the object:")
print (s.size)
print ("The actual data series is:")
print (s.values)
print ("The first two rows of the data series:")
print (s.head(2))

print ("The last two rows of the data series:")
print (s.tail(2))
