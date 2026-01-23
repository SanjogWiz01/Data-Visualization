import pandas as pd
# uses the functon drop_duplicate() to deete 
# the duplicate dat in the table
# example
data={
    'name': [ 'sanjog','microsoft','googrl'],
    'age':[10,20,30],
    'city':['ktm','pkr','ktm']
}
df=pd.DataFrame(data)
print(df)
a1 =df.drop_duplicates()
print(a1)
# true syntex is drop diplicates(subset= ,keep=,inplace=)
a2=df.drop_duplicates(subset='name')
print(a2)
# we can also do thid if we have a multiple tile facing 

# keep function say us what to do with the duplicate value 
a3=df.drop_duplicates(keep='last') # keep last data only
print(a3) 
# keep false delte all deplicate data from the list
