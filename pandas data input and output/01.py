import pandas as pd
# Create a sample DataFrame
data=pd.read_excel('Data Input and Output\Project-Management-Sample-Data.xlsx')
print(data)
# removing duplicates
data_cleaned=data.drop_duplicates()
print("\nData after removing duplicates:")
print(data_cleaned)
# delete certain particular rows
data_cleaned=data_cleaned.drop(index=[47,48,49,50])
print("\nData after deleting specific rows:")
print(data_cleaned)

# for deleting certain column
'''after_column=data_cleaned.drop(columns=['Progress'])
print("\nData after deleting 'Progress' column:")
print(after_column.head())# Deleting a certain column (e.g., 'Progress') '''

# to delete multiple columns
'''after_columns=data_cleaned.drop(columns=['Progress','Start Date'])
print("\nData after deleting 'Progress' and 'Start Date' columns:")
print(after_columns.head()) '''
# to drop duplicate still remaining