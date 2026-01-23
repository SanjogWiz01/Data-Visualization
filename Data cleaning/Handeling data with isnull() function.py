import pandas as pd
data = {
    'Name': ['Sanjog', 'Anil', 'Ram', None],
    'Age': [18, None, 20, 22],
    'City': ['Pokhara', 'Kathmandu', None, 'Butwal']
}
a=pd.DataFrame(data)
print(a)
b=a.isnull()
print(b,'\n\n\n')
# for specific thing
c=pd.isnull(a['Name'])
print(c)