"""
This is code builds a small NN,
it can do a forward pass, it can
also do a backward pass.

No optimization has yet been added
"""
import numpy as np
import nnfs
from nnfs.datasets import spiral_data
nnfs.init()

class Dense_Layer:
    
    def __init__(self, lay_input, lay_neurons):
        # Random init of W and B
        self.weights = np.random.randn(lay_input, lay_neurons) * 0.01
        self.biases = np.zeros((1, lay_neurons))

    # Forward pass
    def forward(self, inputs):
        self.inputs = inputs
        self.output = np.dot(inputs, self.weights) + self.biases

    def backward(self, der):
        self.dweights = np.dot(self.inputs.T, der)
        self.dbiases = np.sum(der, axis = 0, keepdims = True)

        # Grads
        self.dinputs = np.dot(der, self.weights.T)

class Loss:
    
    def get_loss(self, output, y):
        tmp_loss = self.find_loss(output, y)
        mean_loss = np.mean(tmp_loss)
        return mean_loss

class Cat_Cross_Ent(Loss):
    
    def find_loss(self, y_pred, y_gt):
        
        samples = len(y_pred)
        clip_y_pred = np.clip(y_pred, 1e-7, 1 - 1e-7)

        if (len(y_gt.shape) == 1):
            corr_conf = clip_y_pred[range(samples), y_gt]
        
        elif (len(y_gt.shape) == 2):
            corr_conf = np.sum(clip_y_pred * y_gt, axis = 1)

        neg_log_likeli = -np.log(corr_conf)
        return neg_log_likeli

    def backward(self, der, y_gt):
        samples = len(der)
        labels = len(der[0])

        # Sparse -> one-hot
        if (len(y_gt.shape) == 1):
            y_gt = np.eye(labels)[y_gt]

        # Grad calc 
        self.dinputs = -y_gt / der
        
        # Grad normalize
        self.dinputs = self.dinputs / samples

class Cat_Cross_Ent_Back():
    def __init__(self):
        self.activation = Softmax()
        self.loss = Cat_Cross_Ent()
    
    def forward(self, inputs, y_gt):
        self.activation.activate(inputs)
        self.output = self.activation.output
    
        return self.loss.get_loss(self.output, y_gt)

    def backward(self, der, y_gt):
        samples = len(der)

        if (len(y_gt.shape) == 2):
            y_gt = np.argmax(y_gt, axis = 1)

        self.dinputs = der.copy()

        self.dinputs[range(samples), y_gt] -= 1

        self.dinputs = self.dinputs / samples

class ReLU():
    
    def activate(self, inputs):
        self.inputs = inputs
        self.output = np.maximum(0, inputs)

    def backward(self, der):
        self.dinputs = der.copy()
        self.dinputs[self.inputs <= 0] = 0

class Softmax:
    
    def activate(self, inputs):
        # Minus the maximum -> prevent overflow
        exp_values = np.exp(inputs) - np.max(inputs, axis = 1, keepdims = True)
        norm = np.sum(exp_values, axis = 1, keepdims = True)
        prob_dist = exp_values / norm 
        self.output = prob_dist

    def backward(self, der):
        self.dinputs = np.empty_like(der)

        for i, (single_output, single_der) in enumerate(zip(self.output, der)):
            single_output = single_output.reshape(-1, 1)

            jacobian = np.diagflat(single_output) - np.dot(single_output, single_output.T)

            self.dinputs[i] = np.dot(jacobian, single_der)


X, y = spiral_data(samples = 100, classes = 3)

d1 = Dense_Layer(2, 3)
a1 = ReLU()

d2 = Dense_Layer(3, 3)
a2 = Softmax()

loss_func = Cat_Cross_Ent_Back()

d1.forward(X)
a1.activate(d1.output)

d2.forward(a1.output)

loss = loss_func.forward(d2.output, y)

# Back Pass
loss_func.backward(loss_func.output, y)
d2.backward(loss_func.dinputs)
a1.backward(d2.dinputs)
d1.backward(a1.dinputs)



print(d1.dweights)
print(d1.dbiases)
print(d2.dweights)
print(d2.dbiases)

# Cycle, no opt, random assign W + B every iter
#for i in range(100000):
#    d1.weights += 0.05 * np.random.randn(2, 3)
#    d1.biases += 0.05 * np.random.randn(1, 3)
#
#    d2.weights += 0.05 * np.random.randn(3, 3)
#    d2.biases += 0.05 * np.random.randn(1, 3)
#
#    d1.forward(X)
#    a1.activate(d1.output)
#    d2.forward(a1.output)
#    a2.activate(d2.output)
#
#    loss = loss_func.get_loss(a2.output, y)
#
#    preds = np.argmax(a2.output, axis = 1)
#    acc = np.mean(preds == y)
