import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 25, 30]

plt.plot(
    x, y,
    color='blue',           # Line color
    marker='o',             # Marker shape
    markersize=10,          # Marker size
    markerfacecolor='yellow', # Marker fill color
    markeredgecolor='red',  # Marker border color
    linewidth=2             # Line thickness
)

plt.title("Markers in Matplotlib Example")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.show()
