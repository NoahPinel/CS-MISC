import matplotlib.pyplot as plt

def set_plot_settings():
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.axhline(0, color='black', linewidth=1)
    plt.axvline(0, color='black', linewidth=1)
    plt.axis([-10, 10, -1, 10])
