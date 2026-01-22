# uses code like d.read_csv(), df.head(), df.tail(),
# df.info(), df.describe(), df.dropna(),
# df.fillna(), df.isnull()
''' 🧩 Summary Table
Function	Purpose	Example
pd.read_csv()	Read CSV file	pd.read_csv('file.csv')
df.head()	First 5 rows	df.head()
df.tail()	Last rows	df.tail(3)
df.info()	DataFrame info	df.info()
df.describe()	Stats summary	df.describe()
df.dropna()	Remove missing rows	df.dropna()
df.fillna()	Fill missing data	df.fillna({'Age': 20})
df.isnull()	Check missing data	df.isnull()'''
# =============================
# Pandas Data Inspection & Cleaning
# =============================

import pandas as pd

# --- Step 1: Create or Load Data ---
data = {
    'Name': ['Ram', 'Sita', 'Hari', 'Gita', None],
    'Age': [20, 21, None, 22, 23],
    'Marks': [85, 90, 78, None, 88]
}

# You can also load from CSV like this:
# df = pd.read_csv('students.csv')
df = pd.DataFrame(data)
print("=== Original DataFrame ===")
print(df, "\n")

# --- Step 2: View Top and Bottom Rows ---
print("=== Head (first 3 rows) ===")
print(df.head(3), "\n")

print("=== Tail (last 2 rows) ===")
print(df.tail(2), "\n")

# --- Step 3: View DataFrame Info ---
print("=== DataFrame Info ===")
print(df.info(), "\n")

# --- Step 4: Statistical Summary ---
print("=== Statistical Summary ===")
print(df.describe(), "\n")

# --- Step 5: Check Missing Values ---
print("=== Missing Value Check (True = Missing) ===")
print(df.isnull(), "\n")

print("=== Total Missing Values per Column ===")
print(df.isnull().sum(), "\n")

# --- Step 6: Drop Missing Values ---
print("=== Data After Dropping Rows with Any Missing Value ===")
print(df.dropna(), "\n")

# --- Step 7: Fill Missing Values ---
print("=== Data After Filling Missing Values ===")
df_filled = df.fillna({
    'Name': 'Unknown',
    'Age': df['Age'].mean(),
    'Marks': df['Marks'].mean()
})
print(df_filled, "\n")

# --- Step 8: (Optional) Save Cleaned Data to CSV ---
# df_filled.to_csv('cleaned_students.csv', index=False)
# print("Cleaned data saved as 'cleaned_students.csv'")

