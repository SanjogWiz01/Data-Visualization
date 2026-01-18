import pandas as pd
# Data lists
data1 = {
    'name': ['SANJOG', 'POUDEL', 'ANIL'],
    'AGE': [45, 27, 30]
}
data2 = {
    'name': ['RAM', 'SHYAM', 'GITA'],
    'AGE': [20, 25, 22]
}
df = pd.DataFrame(data1)
df1 = pd.DataFrame(data2,index=[3, 4, 5])
print(df)
print(df1)
print("After concatenating two dataframes")
# Concatenating dataframes
print('\n\n\n\n\n\n\n\n\n\n')
frames=[df,df1]
a=pd.concat(frames)
print(a,'\n\n\n\n\n')
print(a.sort_values(by='AGE').reset_index(drop=True))
print('\n\n\n\n\n')
# ignore the index
res2 = pd.concat([df, df1], axis=1, join='inner')

res2 = res2.reset_index(drop=True)
print(res2)
res = pd.concat([df, df1], ignore_index=True)
 
res = res.reset_index(drop=True)
print(res)
