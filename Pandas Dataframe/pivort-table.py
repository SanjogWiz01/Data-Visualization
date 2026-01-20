# importing pandas
import pandas as pd

# creating dataframe
df = pd.DataFrame({'Product': ['Carrots', 'Broccoli', 'Banana', 'Banana',
                               'Beans', 'Orange', 'Broccoli', 'Banana'],
                   'Category': ['Vegetable', 'Vegetable', 'Fruit', 'Fruit',
                                'Vegetable', 'Fruit', 'Vegetable', 'Fruit'],
                   'Quantity': [8, 5, 3, 4, 5, 9, 11, 8],
                   'Amount': [270, 239, 617, 384, 626, 610, 62, 90]})
print(df,'\n\n\n\n\n')
#pivot table
pivot_table = df.pivot_table(index=['Product'],
                       values=['Amount'],
                       aggfunc='sum')
print(pivot_table,'\n\n\n\n\n')\
    #pivot table with multiple aggregation functions
print("here is a data after the isertion of the your requested code snippet")
pivot = df.pivot_table(index=['Product', 'Category'],
                       values=['Amount'], aggfunc='sum')
print(pivot,'\n\n\n\n\n')
outpue=df.pivot_table(index=['Product', 'Category'],
                       values=['Amount'], aggfunc=['sum','mean','max','min'])
print(outpue)
pivot2= df.pivot_table(index=['Product'], values=['Amount'],
                       aggfunc={'median', 'mean', 'min', 'sum', 'max','std'})
print(pivot2)
