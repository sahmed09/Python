import pandas as pd
import numpy as np
from io import StringIO, BytesIO

data = ('col1,col2,col3\n'
        'x,y,1\n'
        'a,b,2\n'
        'c,d,3')
print(type(data))

df = pd.read_csv(StringIO(data))
print(df)

# Convert data into csv file
# df.to_csv('Datasets/Test1.csv')

# Read from specific columns
df = pd.read_csv(StringIO(data), usecols=['col1', 'col2'])
print(df)

df = pd.read_csv(StringIO(data), usecols=lambda x: x.upper() in ['COL1', 'COL3'])
print(df)

# Specifying columns data types
data = ('a,b,c,d\n'
        '1,2,3,4\n'
        '5,6,7,8\n'
        '9,10,11')
print(data)

df = pd.read_csv(StringIO(data), dtype=object)
print(df)
print(df['a'])
print(df['a'][1])
print(type(df['a'][1]))

data = ('a,b,c,d\n'
        '1,2,3,4\n'
        '5,6,7,8\n'
        '9,10,11,12')
print(data)
df = pd.read_csv(StringIO(data), dtype=float)
print(df)
print(type(df['a'][1]))

df = pd.read_csv(StringIO(data), dtype={'b': int, 'c': np.float64, 'a': 'Int64'})
print(df)
print(df.dtypes)
print(df['a'][1], type(df['a'][1]))
print(df['c'][1], type(df['c'][2]))

# Index columns
data = ('index,a,b,c\n'
        '4,apple,bat,5.7\n'
        '8,orange,cow,10')
df = pd.read_csv(StringIO(data))
print("Without Index Column:\n", df)
df = pd.read_csv(StringIO(data), index_col=0)
print("With Index Column:\n", df)

data = ('a,b,c\n'
        '4,apple,bat,\n'
        '8,orange,cow,')
df = pd.read_csv(StringIO(data))
print(df)
df = pd.read_csv(StringIO(data), index_col=False)
print(df)

# Combining usecols and index_col
data = ('a,b,c\n'
        '4,apple,bat,\n'
        '8,orange,cow,')
df = pd.read_csv(StringIO(data), usecols=['b', 'c'], index_col=False)
print(df)

# Quoting and Escape Characters¶. Very useful in NLP
data = 'a,b\n"hello, \\"Bob\\", nice to see you",5'
df = pd.read_csv(StringIO(data), escapechar='\\')
print(df)

# URL to CSV
# df = pd.read_csv('https://download.bls.gov/pub/time.series/cu/cu.item', sep='\t')
# print(df.head())
