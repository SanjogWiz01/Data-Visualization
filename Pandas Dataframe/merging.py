import pandas as pd
# creating first dataframe
data1 = {'key': ['A', 'B', 'C', 'D'],
            'value1': [1, 2, 3, 4]}
df1 = pd.DataFrame(data1)
print(df1,'\n\n\n\n\n')
# creating second dataframe
data2 = {'key': ['B', 'C', 'D', 'E'],
            'value2': [5, 6, 7, 8]}
df2 = pd.DataFrame(data2)
print(df2,'\n\n\n\n\n')
res = pd.merge(df1, df2, on='key')
print(res,'\n\n\n\n\n')
res3 = pd.merge(df1, df2, how='inner', on=['key', 'key1'])
print(res3) # ERROEOO --- IGNORE ---40404040440404