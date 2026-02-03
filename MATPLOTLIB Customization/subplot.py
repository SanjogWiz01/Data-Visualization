import matplotlib.pyplot as plt
import numpy as np

# Creating subplots
fig, ax = plt.subplots(3, 3)

# Plot random data in each subplot
for row in ax:
    for col in row:
        col.plot(np.random.randint(0, 5, 5), np.random.randint(0, 5, 5))

plt.show()