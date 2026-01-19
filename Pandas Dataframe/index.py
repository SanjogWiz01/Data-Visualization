import pandas as pd

data = {'Name': ['John', 'Alice', 'Bob', 'Eve', 'Charlie'],
        'Age': [25, 30, 22, 35, 28],
        'Gender': ['Male', 'Female', 'Male', 'Female', 'Male'],
        'Salary': [50000, 55000, 40000, 70000, 48000]}

df = pd.DataFrame(data)
print(df.index)  # Accessing the index of the DataFrame
print(df)  # Display the DataFrame
print(df.columns) # Accessing only the columns of the DataFrame
print(df.iloc[0])  # Accessing the first row using iloc
print(df['Name'])  # Accessing the 'Name' column
print(df[['Name', 'Age']])  # Accessing multiple columns
print(df.at[0, 'Name'])  # Accessing a specific value using at
print(df.iat[0, 0])  # Accessing a specific value using i


# Access the row at index 1 (second row)
second_row = df.iloc[1]
print(second_row)
# Access rows where 'Age' is greater than 25
filtered_data = df[df['Age'] > 25]
print(filtered_data)