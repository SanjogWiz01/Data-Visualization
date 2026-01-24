import pandas as pd

data = {
    "Name": [
        "  Ram Sharma  ",
        "sita khadka",
        "BISHAL THAPA",
        "  nepal prasad  ",
        "Hari Pokhrel",
        "roshan lama",
        "ANITA RAI",
        "  bikash gurung ",
        "Suman Karki",
        "nisha shrestha"
    ],
    "City": [
        " Kathmandu ",
        "pokhara",
        "BIRATNAGAR",
        " lalitpur ",
        "Bhaktapur",
        "Dharan",
        " ITAHARI ",
        "hetauda",
        "Janakpur",
        " BUTWAL "
    ]
}

df = pd.DataFrame(data)

print("Original DataFrame")
print(df)

df["Name_stripped"] = df["Name"].str.strip()
df["City_stripped"] = df["City"].str.strip()

df["Name_upper"] = df["Name_stripped"].str.upper()
df["Name_lower"] = df["Name_stripped"].str.lower()

df["City_upper"] = df["City_stripped"].str.upper()
df["City_lower"] = df["City_stripped"].str.lower()

df["Name_isupper"] = df["Name_stripped"].str.isupper()
df["Name_islower"] = df["Name_stripped"].str.islower()

df["Name_length"] = df["Name_stripped"].str.len()

df["Starts_with_R"] = df["Name_stripped"].str.startswith("R")

df["Name_split"] = df["Name_stripped"].str.split(" ")

df["Find_a_index"] = df["Name_stripped"].str.find("a")

df["Name_replace"] = df["Name_stripped"].str.replace("a", "@", regex=False)

df["City_replace"] = df["City_stripped"].str.replace("a", "A", regex=False)

print("\nAfter String Cleaning Operations")
print(df)

cleaned_df = df[[
    "Name_stripped",
    "City_stripped",
    "Name_upper",
    "Name_lower",
    "Name_isupper",
    "Name_islower",
    "Name_length",
    "Starts_with_R",
    "Name_split",
    "Find_a_index",
    "Name_replace",
    "City_replace"
]]

cleaned_df.to_csv("cleaned_string_data.csv", index=False)

print("\nCleaned data written to cleaned_string_data.csv")
