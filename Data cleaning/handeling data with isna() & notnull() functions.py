import pandas as pd
data = {
    'Name': ['Sanjog', 'Anil', 'Ram', None],
    'Age': [18, None, 20, 22],
    'City': ['Pokhara', 'Kathmandu', None, 'Butwal']
}
a=pd.DataFrame(data)
b=pd.isna(a['Name'])
print(b) # similar 
# also we have not not null function which is also same as that 
# pandas op in the chat spa guyzzzzzzzzzzzzzzzzz


