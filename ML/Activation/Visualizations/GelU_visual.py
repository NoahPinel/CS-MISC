"""
GeLU implementation
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import special
import visual

def GeLU(x):
    err = 1 + special.erf(x / np.sqrt(2))
    gelooooood = (0.5) * x * err
    return gelooooood

x = np.linspace(-10, 10, 100)
y = GeLU(x)

visual.set_plot_settings()
plt.plot(x, y)
plt.show()
