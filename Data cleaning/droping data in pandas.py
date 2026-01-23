import pandas as pd
data = {
    'Name': ['Sanjog', 'Anil', 'Ram', None],
    'Age': [18, None, 20, 22],
    'City': ['Pokhara', 'Kathmandu', None, 'Butwal']
}
df=pd.DataFrame(data)
# droping the data
a=df.dropna() # delte all data which are incomplete to the syesyem all table and rows
print(a,'\n\n\n')
b=df.dropna(how='all') # delte only which have all mising values in the givrn data 
print(b,'\n\n\n\n')
c=df.dropna(axis=1)
print(c)
d=df.dropna(axis=0,how='any')
print(d)
# len(df.dropna()) this is used to find the length of the guven data
