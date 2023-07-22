"""
Code that simulates the softmax function
given data set of size n, generate a prob.
dist. -> [0, 1].
"""
import numpy as np

def calc_soft(points):
    exp_values = np.exp(points)
    norm = np.sum(exp_values)
    prob_dist = exp_values / norm
    return prob_dist

num_values = int(input('Enter # of data points: '))
value_min = 0
value_max = 100

points = np.random.uniform(value_min, value_max, num_values)
x = calc_soft(points)

print('Raw input:\n', points)
print('Probability distribution:\n', x)

sum_prob_dist = np.sum(x)
print(f'Sum = {sum_prob_dist:.1f}')
