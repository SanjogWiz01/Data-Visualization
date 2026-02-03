import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 20, 15, 25]

plt.figure(figsize=(8, 4))  # width=8 inches, height=4 inches
plt.plot(x, y, marker='o')

plt.title("Resized Plot Example")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()
