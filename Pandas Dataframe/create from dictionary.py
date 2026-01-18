import pandas as pd

# Sample dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Paris', 'London']
}

# Create DataFrame from dictionary
df = pd.DataFrame(data)

print(df)
# created from dictionary