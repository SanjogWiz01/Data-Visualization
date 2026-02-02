import pandas as pd

series = pd.Series(['New York', 'Chicago', 'Toronto', 'Lisbon'])

# Creating the row axis labels
series.index = ['City 1', 'City 1', 'City 3', 'City 3'] 
print(series)

# also 
series = pd.Series(['New York', 'Chicago', 'Toronto', 'Lisbon'],index = ['City 1', 'City 1', 'City 3', 'City 3'])
print(series)
