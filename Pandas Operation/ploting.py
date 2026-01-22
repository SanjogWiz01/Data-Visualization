import pandas as pd
import matplotlib.pyplot as plt

# Sample data
data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
    'Sales': [2500, 2700, 3000, 3200, 3600, 4000],
    'Profit': [500, 600, 650, 700, 900, 1000],
    'Expenses': [2000, 2100, 2350, 2500, 2700, 3000]
}

df = pd.DataFrame(data)
print(df)
# Line plot for Sales over Months
plt.figure(figsize=(8,5))
plt.plot(df['Month'], df['Sales'], marker='o', label='Sales')
plt.plot(df['Month'], df['Profit'], marker='s', label='Profit', color='green')
plt.title("Sales and Profit Over Months")
plt.xlabel("Month")
plt.ylabel("Amount (in Rs)")
plt.legend()
plt.grid(True)
plt.show()
