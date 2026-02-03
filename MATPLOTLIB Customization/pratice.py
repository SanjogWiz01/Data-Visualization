import matplotlib.pyplot as plt
import numpy as np

# Sample data
x = np.arange(1, 11)
y1 = x * 2
y2 = x ** 1.5

# 1. Create a figure and resize the plot
plt.figure(figsize=(10, 6))  # Resize a plot in Matplotlib

# 2. Plot with markers and transparency
plt.plot(
    x, y1,
    marker='o',              # Markers in Matplotlib
    linestyle='-',
    linewidth=2,
    alpha=0.8,               # Adjust Plot Transparency
    label='y = 2x'
)

plt.plot(
    x, y2,
    marker='s',
    linestyle='--',
    linewidth=2,
    alpha=0.8,
    label='y = x^1.5'
)

# 3. Adding labels and title
plt.xlabel('X Values', fontsize=12)   # Adding Labels in Matplotlib
plt.ylabel('Y Values', fontsize=12)
plt.title('Matplotlib Customization Demo', fontsize=14)

# 4. Move axis labels
plt.xlabel('X Values', labelpad=15)    # Move Axis Labels in Matplotlib
plt.ylabel('Y Values', labelpad=15)

# 5. Configure grid
plt.grid(True, linestyle=':', linewidth=1, alpha=0.7)  # Configuring Grid

# 6. Change fonts
plt.title('Matplotlib Customization Demo', fontname='DejaVu Sans', fontsize=14)
plt.xlabel('X Values', fontname='DejaVu Sans', fontsize=12)
plt.ylabel('Y Values', fontname='DejaVu Sans', fontsize=12)

# 7. Set tick label font size
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)

# 8. Change plot background color
ax = plt.gca()
ax.set_facecolor('#f2f2f2')  # Light gray background

# 9. Add legend
plt.legend()

# Show the first customized plot
plt.tight_layout()
plt.show()

# =========================
# 10. Creating Subplots in Matplotlib
# =========================

fig, axes = plt.subplots(2, 1, figsize=(10, 8))

# First subplot
axes[0].plot(x, y1, color='blue', marker='o', label='y = 2x')
axes[0].set_title('First Subplot: y = 2x')
axes[0].set_xlabel('X')
axes[0].set_ylabel('Y')
axes[0].grid(True)
axes[0].legend()

# Second subplot
axes[1].plot(x, y2, color='green', marker='s', label='y = x^1.5')
axes[1].set_title('Second Subplot: y = x^1.5')
axes[1].set_xlabel('X')
axes[1].set_ylabel('Y')
axes[1].grid(True)
axes[1].legend()

plt.tight_layout()
plt.show()

# =========================
# 11. Styling Plots with Matplotlib
# =========================

plt.style.use('ggplot')  # Apply a style

plt.figure(figsize=(8, 5))
plt.plot(x, y1, marker='o', label='y = 2x')
plt.plot(x, y2, marker='s', label='y = x^1.5')
plt.title('Styled Plot using ggplot Style')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.tight_layout()
plt.show()

# =========================
# 12. Hide Axis, Borders and Extra Space
# =========================

plt.figure(figsize=(8, 5))
plt.plot(x, y1, marker='o')

# Hide axis
plt.axis('off')  # Hide Axis

# Remove extra space
plt.margins(0)

plt.title('Plot with Hidden Axis and No Extra Space')
plt.tight_layout()
plt.show()
