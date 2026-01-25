import pandas as pd
df = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/nba.csv")

team = df.groupby('Team')
print(team.first()) # Let's print the first entries in all the groups formed.


# grouping by multiple columns
grouping = df.groupby(['Team', 'Position'])
print(grouping.first())

# grouping using aggregate functions
aggregated_data = df.groupby(['Team', 'Position']).agg(
    total_salary=('Salary', 'sum'),
    avg_salary=('Salary', 'mean'),
    player_count=('Name', 'count')
)

print(aggregated_data)

#transforming data within groups
df['Rank within Team'] = df.groupby('Team')['Salary'].transform(lambda x: x.rank(ascending=False))
print(df)
# Filtering groups based on a condition
filtered_df = df.groupby('Team').filter(lambda x: x['Salary'].mean() >= 1000000)
print(filtered_df)