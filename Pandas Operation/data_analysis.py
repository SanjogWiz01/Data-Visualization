import pandas as pd
df = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")

team = df.groupby('Team')
print(team.first()) # Let's print the first entries in all the groups formed.


