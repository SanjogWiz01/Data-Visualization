import pandas as pd

# -----------------------------
# 1. Creating a DataFrame
# -----------------------------
data = {
    "Name": ["Ram", "Shyam", "Hari", "Sita", "Gita"],
    "Age": [22, 25, 30, 28, 26],
    "City": ["Pokhara", "Kathmandu", "Butwal", "Dharan", "Biratnagar"],
    "Score": [85, 90, 88, 70, 95]
}

df = pd.DataFrame(data)
print("\n1. DataFrame:\n", df)

# -----------------------------
# 2. Pandas DataFrame Index
# -----------------------------
print("\n2. Index:\n", df.index)   # Row indexes
print("\n2. Columns:\n", df.columns)  # Column labels

# -----------------------------
# 3. Access DataFrame
# -----------------------------
print("\n3. Access single column:\n", df["Name"])
print("\n3. Access multiple columns:\n", df[["Name", "City"]])

# -----------------------------
# 4. Indexing and Selecting Data
# -----------------------------
print("\n4. Using loc (label-based):\n", df.loc[0, "Name"])   # First row, Name
print("\n4. Using iloc (position-based):\n", df.iloc[2, 1])   # 3rd row, 2nd column
print("\n4. Select rows by condition:\n", df.loc[df["Age"] > 25])

# -----------------------------
# 5. Slicing Pandas DataFrame
# -----------------------------
print("\n5. Row slicing (first 3 rows):\n", df[:3])
print("\n5. Column slicing:\n", df.iloc[:, 1:3])

# -----------------------------
# 6. Filter with Multiple Conditions
# -----------------------------
print("\n6. Filter (Age > 25 and Score > 80):\n", df[(df["Age"] > 25) & (df["Score"] > 80)])

# -----------------------------
# 7. Merging, Joining and Concatenating DataFrames
# -----------------------------
data2 = {
    "Name": ["Ram", "Shyam", "Hari", "Sita", "Gita"],
    "Department": ["CSE", "ECE", "ME", "CE", "IT"]
}
df2 = pd.DataFrame(data2)

# Merge on "Name"
merged = pd.merge(df, df2, on="Name")
print("\n7. Merged DataFrame:\n", merged)

# Concatenate
concat_df = pd.concat([df, df2], axis=1)
print("\n7. Concatenated DataFrame:\n", concat_df)

# -----------------------------
# 8. Sorting Pandas DataFrame
# -----------------------------
print("\n8. Sort by Age:\n", df.sort_values(by="Age"))
print("\n8. Sort by Score (descending):\n", df.sort_values(by="Score", ascending=False))

# -----------------------------
# 9. Pivot Table in Pandas
# -----------------------------
# Example dataset for pivot table
data3 = {
    "Department": ["CSE", "ECE", "CSE", "ECE", "CSE"],
    "Gender": ["M", "F", "M", "M", "F"],
    "Score": [85, 90, 88, 70, 95]
}
df3 = pd.DataFrame(data3)

pivot = pd.pivot_table(df3, values="Score", index="Department", columns="Gender", aggfunc="mean")
print("\n9. Pivot Table:\n", pivot)
print("\nSummary Complete.",'\n8')
print("here is a data after the isertion of the your requested code snippet")