import pandas as pd

# reading csv file 
df = pd.read_csv("Data Input and Output (I/people.csv") # copy the path and paste it easy
print(df)
# reading specific colums 
print('\n\n\nnnnn')
df = pd.read_csv("Data Input and Output (I/people.csv", usecols=["First Name", "Email"])
print(df)
# reading rows
df = pd.read_csv("Data Input and Output (I\people.csv", index_col="Job Title")
print('\n\n\n\n\n',df)
#
f = pd.read_csv("Data Input and Output (I\people.csv",  na_values=["N/A", "Unknown"])
print('\n\n\n\n\n',df)