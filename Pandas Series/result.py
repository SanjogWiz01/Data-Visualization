import pandas as pd

# Read the Excel file
df = pd.read_excel('Nursing.xlxs.xlsx')

# Sort the dataframe (by first column, ascending)
df_sorted = df.sort_values(by=df.columns[0])

# Display the sorted data
print(df_sorted)

# Optional: Save the sorted data to a new Excel file
df_sorted.to_excel('Nursing.xlxs.xlsx', index=False)