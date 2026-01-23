import pandas as pd

# Creating a DataFrame with mixed types in different columns
data = {
    'ID': [101, 102, 103, '104', 105],
    'Name': ['Sanjog', 'Anil', 'Rita', 'Kiran', 123],
    'Age': [25, 'Thirty', 22, 28, 30],
    'Salary': [30000, 25000, 'Thirty-five thousand', 32000, 40000],
    'Department': ['IT', 'HR', 'Finance', 'IT', 100]
}

df = pd.DataFrame(data)

print("Original DataFrame:")
print(df)
print("\n\n")

# Step 1: Check the data types of each column
print("Data types of each column:")
print(df.dtypes)
print("\n\n")

# Step 2: Detect if any column has mixed types
print("Detecting mixed datatypes in each column:")
for col in df.columns:
    types_found = df[col].apply(type).unique()
    if len(types_found) > 1:
        print(f"Column '{col}' has mixed types: {types_found}")
    else:
        print(f"Column '{col}' is uniform type: {types_found[0]}")
print("\n\n")

# Step 3: Optionally, get a list of all columns with mixed types
mixed_columns = [col for col in df.columns if len(df[col].apply(type).unique()) > 1]
print("Columns with mixed data types:", mixed_columns)
