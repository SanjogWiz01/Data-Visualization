import pandas as pd
import numpy as np

data = {
    'Name': ['Sanjog', 'Anil', 'Ram', None],
    'Age': [18, None, 20, 22],
    'City': ['Pokhara', 'Kathmandu', None, 'Butwal']
}

df = pd.DataFrame(data)
print("Original Data:\n", df)

# Replace missing values (None) with a default value
df1 = df.replace(to_replace=np.nan, value=-99) 


print("\nAfter Replacing Missing Data:\n", df1,'\n\n\nnnnnn')
# can be replace also to a specific terem also 
df2=df['Age'].replace(to_replace=np.nan, value=-99)
print(df2)
# df.interpolate() also functio likr tbis occur to the system for data procoessing 
a=df.interpolate()
print(a)
