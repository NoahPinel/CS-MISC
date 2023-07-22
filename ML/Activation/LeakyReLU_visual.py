"""
Code to visualize ReLU function
but with a leak param now
"""
import numpy as np
import matplotlib.pyplot as plt

def LReLU(x):
    rect = []
    leak = 0.1
    for point in x:
        rect.append(max(leak * point, point))
    return np.array(rect, dtype=float)


x = np.linspace(-5, 10, 100)
y = LReLU(x)


plt.plot(x, y)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)
plt.axis([-10, 10, -10, 10])
plt.show()
