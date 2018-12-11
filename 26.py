import pandas as pd
s = pd.Series(["a","b","c","a"], dtype="category")
print (s)
cat = pd.Categorical(['a', 'b', 'c', 'a', 'b', 'c'])
print (cat)
cat = cat=pd.Categorical(['a','b','c','a','b','c','d'], ['c', 'b', 'a'])
print (cat)
cat =pd.Categorical(['a','b','c','a','b','c','d'], ['c', 'b', 'a'],ordered=True)
print (cat)

s = pd.Series(["a","b","c","a"], dtype="category")
s = s.cat.add_categories([4])
print (s.cat.categories)
print (s.cat.remove_categories("a"))

