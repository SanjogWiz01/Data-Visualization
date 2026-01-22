import pandas as pd

# You can use an online CSV or make your own
url = "https://people.sc.fsu.edu/~jburkardt/data/csv/hw_200.csv"
df = pd.read_csv(url)

# Clean column names (remove spaces and quotes)
df.columns = df.columns.str.replace('"', '').str.strip()
df.rename(columns={'Height(Inches)': 'Height_in', 'Weight(Pounds)': 'Weight_lb'}, inplace=True)

# Show first few rows
print("Sample data:\n", df.head(), "\n")

# === Basic Correlation ===
corr_matrix = df.corr()
print("Correlation Matrix:\n", corr_matrix, "\n")

# Example: find correlation between Height and Weight only
print("Correlation between Height and Weight:")
print(df['Height_in'].corr(df['Weight_lb']))