import pandas as pd

data = {
    "id": [1, 2, 3, 4, 5],
    "name": ["Ram Sharma", "Sita Khadka", "Bishal Thapa", "Nisha Rai", "Hari Pokhrel"],
    "city": ["Kathmandu", "Pokhara", "Butwal", "Dharan", "Lalitpur"],
    "salary": [50000, 48000, 52000, 47000, 51000]
}

df = pd.DataFrame(data)

print("Original DataFrame")
print(df)

df.to_csv("employees.csv", index=False)
print("\nData exported to employees.csv")

df_csv = pd.read_csv("employees.csv")
print("\nRead CSV File")
print(df_csv)

df_csv.to_csv("employees_exported.csv", index=False)
print("\nData exported again to employees_exported.csv")

df.to_json("employees.json", orient="records", indent=4, force_ascii=False)
print("\nData exported to employees.json")

df_json = pd.read_json("employees.json")
print("\nRead JSON File")
print(df_json)

df_json.to_json("employees_exported.json", orient="records", indent=4, force_ascii=False)
print("\nParsed JSON and exported to employees_exported.json")

df.to_excel("employees.xlsx", index=False)
print("\nData exported to employees.xlsx")

df_excel = pd.read_excel("employees.xlsx")
print("\nRead Excel File")
print(df_excel)

text_data = """id,name,city,salary
6,Anita Gurung,Hetauda,49000
7,Suman Karki,Janakpur,46000
8,Rita Shrestha,Butwal,53000
"""

with open("employees.txt", "w", encoding="utf-8") as f:
    f.write(text_data)

print("\nText file employees.txt created")

df_text = pd.read_csv("employees.txt")
print("\nRead Text File using Pandas")
print(df_text)

df_text.to_csv("employees_from_text.csv", index=False)
print("\nText file converted to CSV: employees_from_text.csv")

print("\nAll Pandas I/O operations completed successfully")
# --- IGNORE ---  