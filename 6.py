##DataFrame Basic Functionality
##S.No. 	Attribute or Method 	Description
##1 	T 	Transposes rows and columns.
##2 	axes 	Returns a list with the row axis labels and column axis labels as the only members.
##3 	dtypes 	Returns the dtypes in this object.
##4 	empty 	True if NDFrame is entirely empty [no items]; if any of the axes are of length 0.
##5 	ndim 	Number of axes / array dimensions.
##6 	shape 	Returns a tuple representing the dimensionality of the DataFrame.
##7 	size 	Number of elements in the NDFrame.
##8 	values 	Numpy representation of NDFrame.
##9 	head() 	Returns the last n rows.
##10 	tail() 	Returns last n rows.
import pandas as pd
import numpy as np

#Create a Dictionary of series
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Smith','Jack']),
   'Age':pd.Series([25,26,25,23,30,29,23]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8])}

#Create a DataFrame
df = pd.DataFrame(d)
print ("Our data series is:")
print(df)
print(df.T)

print ("Row axis labels and column axis labels are:")
print (df.axes)

print ("The data types of each column are:")
print (df.dtypes)

print ("The dimension of the object is:")
print (df.ndim)

print ("The shape of the object is:")
print (df.shape)

print ("The total number of elements in our object is:")
print (df.size)


print ("The actual data in our data frame is:")
print (df.values)

print ("The first two rows of the data frame is:")
print (df.head(2))


print ("The last two rows of the data frame is:")
print (df.tail(2))
