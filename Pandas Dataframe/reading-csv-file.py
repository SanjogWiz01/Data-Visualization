import pandas as pd
df = pd.read_csv(r'C:\Users\sanjo\OneDrive\Desktop\Pandas\Pandas Dataframe\problem1.csv', encoding='latin1')
print(df)
print(df.shape)
print('\n ',df.info())