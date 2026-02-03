import matplotlib.pyplot as plt
import numpy as np
# Generate random data for subplots
labels = ['Category 1', 'Category 2', 'Category 3']
sizes1 = np.random.randint(1, 10, 3)
sizes2 = np.random.randint(1, 10, 3)
sizes3 = np.random.randint(1, 10, 3)

# Create subplots with pie charts
fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(12, 4))

axes[0].pie(sizes1, labels=labels, autopct='%1.1f%%', colors=['lightcoral', 'lightblue', 'lightgreen'])
axes[1].pie(sizes2, labels=labels, autopct='%1.1f%%', colors=['gold', 'lightseagreen', 'lightpink'])
axes[2].pie(sizes3, labels=labels, autopct='%1.1f%%', colors=['lightskyblue', 'lightgreen', 'lightcoral'])

# Add titles
axes[0].set_title('Pie Chart 1')
axes[1].set_title('Pie Chart 2')
axes[2].set_title('Pie Chart 3')

# Adjust layout for better spacing
plt.tight_layout()

# Display the figure
plt.show()
