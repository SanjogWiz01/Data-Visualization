import pandas as pd
import numpy as np

# Create a DataFrame from a dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 28],
    'Salary': [50000, 60000, 75000, 65000],
    'Department': ['Sales', 'IT', 'HR', 'Finance']
}

df = pd.DataFrame(data)

# Display basic information
print(df)
print("\nDataFrame Info:")
print(df.info())
print("\nStatistical Summary:")
print(df.describe())

# Access columns and rows
print("\nNames:", df['Name'].tolist())
print("\nFirst row:\n", df.iloc[0])

# Filter data
high_salary = df[df['Salary'] > 60000]
print("\nEmployees with salary > 60000:\n", high_salary)

# Add a new column
df['Bonus'] = df['Salary'] * 0.1
print("\nDataFrame with Bonus:\n", df)