import pandas as pd

data1 = {'key': ['K0', 'K1', 'K2', 'K3'],
         'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'],
        'Age':[27, 24, 22, 32],}

data2 = {'key': ['K0', 'K1', 'K2', 'K3'],
         'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'],
        'Qualification':['Btech', 'B.A', 'Bcom', 'B.hons']}

df1 = pd.DataFrame(data1)

df2 = pd.DataFrame(data2)
print(df1,'\n\n\n\n\n',df2,'\n\n\n\n\n')
#merging with key
res = pd.merge(df1,df2, on='key')
print(res)