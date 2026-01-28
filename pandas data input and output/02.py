import pandas as pd

# Read Excel file
df = pd.read_excel('2022-FIFA-World-Cup-Performance-Sample-Data.xlsx')

# Remove leading/trailing spaces from column names
df.columns = df.columns.str.strip()

# Print original DataFrame
print('Normal dataframe:\n', df)

# Drop the column
df = df.drop(columns=['Club'])

# Print updated DataFrame
print('\nDataframe after deleting "Club" column:\n', df)