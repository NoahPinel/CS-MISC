"""
ReLU plot code
"""
import numpy as np
import matplotlib.pyplot as plt

def ReLU(x):
    return np.maximum(0, x)

x = np.linspace(-5, 10, 100)
y = ReLU(x)

plt.plot(x, y)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)
plt.axis([-10, 10, -1, 10])  # Adjust the y-axis range to show ReLU behavior better
plt.xlabel('Input (x)')
plt.ylabel('Output (ReLU(x))')
plt.title('ReLU Function')
plt.show()
