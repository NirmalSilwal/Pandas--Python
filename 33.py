import pandas as pd
p =pd.read_csv('temp.csv', nrows=2)
print(p)

chunker = pd.read_csv('temp.csv', chunksize=10)
print(chunker)

for piece in chunker:
    print(piece)

