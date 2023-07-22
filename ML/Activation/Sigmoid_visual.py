"""
Visual representation of the sigmoid activation
function
"""
import numpy as np
import matplotlib.pyplot as plt

def calc_sig(x):
    return 1 / (1 + np.exp(-x))

def sigmoid(x):
    return calc_sig(x)

x_range = np.linspace(-10, 10, 100)

# Generate biased data using a normal distribution around the midpoint of the sigmoid curve
midpoint = 0
variance = 1
num_samples = 50

# Generate biased data using a normal distribution
biased_data = np.random.normal(loc=midpoint, scale=variance, size=num_samples)
y_biased = sigmoid(biased_data)
plt.plot(x_range, sigmoid(x_range), label='Sigmoid Curve')
plt.scatter(biased_data, y_biased, color='red', label='Biased Data')
plt.axhline(0, color='black', linewidth=1.5)  # Bold line at y=0
plt.axvline(0, color='black', linewidth=1.5)  # Bold line at x=0
plt.legend()
plt.grid(True)
plt.show()
