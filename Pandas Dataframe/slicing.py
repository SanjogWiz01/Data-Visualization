# import pandas as pd

# player_list = [['M.S.Dhoni', 36, 75, 5428000],
#                ['A.B.D Villers', 38, 74, 3428000],
#                 ['Chris Gayle', 43, 89, 4000000]]

# df = pd.DataFrame(player_list, columns=['Name', 'Age', 'Weight', 'Salary'])
# print(df)
import pandas as pd
data ={'Name': ['John', 'Alice', 'Bob', 'Eve', 'Charlie'],
        'Age': [25, 30, 22, 35, 28]}
df = pd.DataFrame(data)
print(df)
a= df.iloc[0:4]
print('\n',a)  #slicing
print('\n',df.iloc[-4:-1])  #negative indexing slicing
b=df.iloc[:,0:1]
print('\n',b)  #slicing columns