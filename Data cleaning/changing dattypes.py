import pandas as pd

data = {'Age': [18.5, 20.2, 22.1]}
df = pd.DataFrame(data)

print("Before:\n", df.dtypes)

df['Age'] = df['Age'].astype(int)

print("\nAfter:\n", df.dtypes)
# folat is change into the integer data after this processsssssssssssssssssssssssssssssssssss