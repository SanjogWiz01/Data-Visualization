# from numpy array
import numpy as np
import pandas as pd
data = np.array(['s', 'a', 'n', 'j', 'o','g'])

ser = pd.Series(data)
print(ser) 
# for list
data = ['s', 'a', 'n', 'j', 'o','g']
print('from list is :',pd.Series(data))
# from dictionary
# Creating a small dictionary
my_dictionary = {
    "Benevolent": "Kind and generous",
    "Curious": "Eager to know or learn",
    "Efficient": "Doing tasks with minimal waste",
    "Fragile": "Easily broken or damaged",
    "Harmony": "Peaceful agreement or balance",
    "Innovate": "Introduce new ideas or methods",
    "Jubilant": "Feeling great joy",
    "Modest": "Humble and not boastful",
    "Reliable": "Can be trusted",
    "Vivid": "Clear and detailed in the mind"
}

series=pd.Series(my_dictionary)
print(series)
# using range
seri=pd.Series(range(5,10))
print(seri)
    

