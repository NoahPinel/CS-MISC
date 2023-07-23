"""
A 3 node network, simply calculate
the layer outputs, save to list, print
"""
inputs = [3, 2.7, 1, 1.9]

weight = [[0.3, 0.4, -0.1, 0.69], 
		  [0.23, -0.2, 0.35, 0.43], 
	      [0.5, 0.3, -0.17, -0.91]]
bias = [0.1, 2, 1.5] 


outs = []

# Hop percerptron's
for lay_w, lay_b in zip(weight, bias):
    n_output = 0
    for inp, w in zip(inputs, lay_w):
        n_output += inp * w

    # factor in bias
    n_output += lay_b
    outs.append(n_output)

# Layer output
print(outs)
