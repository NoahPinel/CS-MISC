"""
Code to visualize ReLU function
"""
import numpy as np
import matplotlib.pyplot as plt

def ReLU(x):
    rect = []
    for point in x:
        rect.append(max(0, point))
    return np.array(rect, dtype=float)


x = np.linspace(-5, 10, 100)
y = ReLU(x)

plt.plot(x, y)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)
plt.axis([-10, 10, -10, 10])
plt.show()
