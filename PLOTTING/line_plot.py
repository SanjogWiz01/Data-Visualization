import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 2, 3, 4])  # X-axis 
y = x*2  # Y-axis

plt.plot(x, y)  
plt.xlabel('X-axis Label')
plt.ylabel('Y-axis Label')
plt.title('Line Plot Example')

plt.show()