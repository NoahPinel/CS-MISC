"""
Code that simulates the TanH function
"""
import numpy as np
import matplotlib.pyplot as plt
def Calc_Hyp_Tan(points): 
    numera = np.exp(points) - np.exp(-points)
    denom = np.exp(points) + np.exp(-points)
    tanned_data = numera / denom
    return tanned_data

x = np.linspace(-10, 10, 100)
y = Calc_Hyp_Tan(x)

plt.plot(x, y)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.axhline(0, color='black', linewidth=1)
plt.axvline(0, color='black', linewidth=1)
plt.axis([-4, 4, -1, 1])
plt.show()
