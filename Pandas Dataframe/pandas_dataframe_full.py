
import pandas as pd

df = pd.read_excel("employee_sales_data.xlsx")

print("Full DataFrame")
print(df)

print("\nHead and Tail")
print(df.head())
print(df.tail())

print("\nDataFrame Info")
print(df.info())

print("\nCreating New DataFrame")
data = {"name": ["Sanjog", "Bikash", "Sita"], "salary": [60000, 45000, 70000]}
df_new = pd.DataFrame(data)
print(df_new)

print("\nSetting Index")
df.set_index("emp_id", inplace=True)
print(df)

print("\nAccessing Columns")
print(df["salary"])
print(df[["name", "department", "salary"]])

print("\nIndexing with loc and iloc")
print(df.loc[1])
print(df.iloc[0:5])

print("\nSlicing Data")
print(df.iloc[5:15, 0:4])
print(df.loc[10:20, ["name", "city", "sales"]])

print("\nFiltering with Multiple Conditions")
print(df[(df["department"] == "IT") & (df["sales"] > 15000)])
print(df[(df["city"] == "Pokhara") | (df["salary"] > 75000)])

print("\nSorting Data")
print(df.sort_values(by="sales", ascending=False))

print("\nGrouping and Aggregation")
print(df.groupby("department")["salary"].mean())

print("\nAdding and Dropping Columns")
df["annual_salary"] = df["salary"] * 12
print(df.head())
df = df.drop(columns=["annual_salary"])

print("\nMerging DataFrames")
dept_data = {"department": ["IT", "HR", "Finance"], "manager": ["Ram", "Shyam", "Hari"]}
df_dept = pd.DataFrame(dept_data)
merged_df = pd.merge(df.reset_index(), df_dept, on="department")
print(merged_df.head())

print("\nConcatenating DataFrames")
part1 = df.iloc[:10]
part2 = df.iloc[10:20]
print(pd.concat([part1, part2]))

print("\nPivot Table")
pivot = pd.pivot_table(df.reset_index(), values="sales", index="department", columns="month", aggfunc="sum")
print(pivot)

print("\nExport Cleaned Data")
df.reset_index().to_excel("cleaned_employee_data.xlsx", index=False)
