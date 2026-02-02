import pandas as pd

data = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])

# Accessing the index
print("Original Index:\n", data)

# Modifying the index
data.index = ['w', 'x', 'y', 'z']
print("Modified Series:\n", data)