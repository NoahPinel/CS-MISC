"""
Code that plots ReLU with a leak factor
i.e. leakyReLU
"""
import numpy as np
import matplotlib.pyplot as plt
import visual

def LReLU(x, leak=0.1):
    return np.maximum(leak * x, x)

x = np.linspace(-5, 10, 100)
y = LReLU(x)

visual.set_plot_settings()
plt.plot(x, y)
plt.show()
