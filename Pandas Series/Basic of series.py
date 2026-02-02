# series is a one dimesnion label that can carry any type of data 
'''Key Features of Pandas Series:

Supports integer-based and label-based indexing.
Stores heterogeneous data types.
Offers a variety of built-in methods for data manipulation and analysis.
'''
# create a series in pandas
import pandas as pd
data=['s','a','n']
print(pd.Series(data))
#.series is a pre defined libary in pandas of python

# acessing the data
print(' the acessing element is : ',pd.Series(data)[2])
