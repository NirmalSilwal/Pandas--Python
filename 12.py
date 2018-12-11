##1 	lower() 	Converts strings in the Series/Index to lower case.
##2 	upper() 	Converts strings in the Series/Index to upper case.
##3 	len() 	Computes String length().
##4 	strip() 	Helps strip whitespace(including newline) from each string in the Series/index from both the sides.
##5 	split(' ') 	Splits each string with the given pattern.
##6 	cat(sep=' ') 	Concatenates the series/index elements with given separator.
##7 	get_dummies() 	Returns the DataFrame with One-Hot Encoded values.
##8 	contains(pattern) 	Returns a Boolean value True for each element if the substring contains in the element, else False.
##9 	replace(a,b) 	Replaces the value a with the value b.
##10 	repeat(value) 	Repeats each element with specified number of times.
##11 	count(pattern) 	Returns count of appearance of pattern in each element.
##12 	startswith(pattern) 	Returns true if the element in the Series/Index starts with the pattern.
##13 	endswith(pattern) 	Returns true if the element in the Series/Index ends with the pattern.
##14 	find(pattern) 	Returns the first position of the first occurrence of the pattern.
##15 	findall(pattern) 	Returns a list of all occurrence of the pattern.
##16 	swapcase 	Swaps the case lower/upper.
##17 	islower() 	Checks whether all characters in each string in the Series/Index in lower case or not. Returns Boolean
##18 	isupper() 	Checks whether all characters in each string in the Series/Index in upper case or not. Returns Boolean.
##19 	isnumeric() 	Checks whether all characters in each string in the Series/Index are numeric. Returns Boolean.

import pandas as pd
import numpy as np

import pandas as pd
import numpy as np

s = pd.Series(['Rajiv   \n', 'Sandeep', 'Rahul', 'Bijoy', np.nan, '1234','US'])

print (s)
print(s.str.lower())
print(s.str.upper())
print(s.str.len())
print ("After Stripping:")
print (s.str.strip())
print ("Split Pattern:")
print (s.str.split(' '))
print (s.str.cat(sep='_'))
print (s.str.get_dummies())
print (s.str.contains(' '))
print ("After replacing 3 with 7:")
print (s.str.replace('3','7'))
print (s.str.repeat(2))
print ("The number of '3's in each string:")
print (s.str.count('3'))

print (s.str.findall('S'))
