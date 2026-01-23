import pandas as p
data = {
    'Name': ['Sanjog', 'Anil', 'Ram', None],
    'Age': [18, None, 20, 22],
    'City': ['Pokhara', 'Kathmandu', None, 'Butwal']
}
a=p.DataFrame(data)
b=a.fillna('ktm') # all numm dat will be fille dwith ktm 
print(b)
# some methods are there as well 2 methods 
# pad and b-fill
c=a.fillna(method='pad') # pad means it will automaticallly fills the previous dat to the saytema autmitacally
print(c)
d=a.fillna(method='bfill') #bfilll means fill the dat with the next values
print(d)