"""
Just a test to see how
poorly this performs on
0-9.

And with no suprise it is 
shit...

Also getting an underflow error
in the S.max func
"""
import numpy as np
import nnfs
from tqdm import tqdm
import tensorflow as tf


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
        self.dbiases = np.sum(der, axis=0, keepdims=True)

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

        if len(y_gt.shape) == 1:
            corr_conf = clip_y_pred[range(samples), y_gt]

        elif len(y_gt.shape) == 2:
            corr_conf = np.sum(clip_y_pred * y_gt, axis=1)

        neg_log_likeli = -np.log(corr_conf)
        return neg_log_likeli

    def backward(self, der, y_gt):
        samples = len(der)
        labels = len(der[0])

        # Sparse -> one-hot
        if len(y_gt.shape) == 1:
            y_gt = np.eye(labels)[y_gt]

        # Grad calc
        self.dinputs = -y_gt / der

        # Grad normalize
        self.dinputs = self.dinputs / samples


class Cat_Cross_Ent_Back:
    def __init__(self):
        self.activation = Softmax()
        self.loss = Cat_Cross_Ent()

    def forward(self, inputs, y_gt):
        self.activation.activate(inputs)
        self.output = self.activation.output

        return self.loss.get_loss(self.output, y_gt)

    def backward(self, der, y_gt):
        samples = len(der)

        if len(y_gt.shape) == 2:
            y_gt = np.argmax(y_gt, axis=1)

        self.dinputs = der.copy()

        self.dinputs[range(samples), y_gt] -= 1

        self.dinputs = self.dinputs / samples


class ReLU:
    def activate(self, inputs):
        self.inputs = inputs
        self.output = np.maximum(0, inputs)

    def backward(self, der):
        self.dinputs = der.copy()
        self.dinputs[self.inputs <= 0] = 0


class Softmax:
    def activate(self, inputs):
        self.inputs = inputs
        # Minus the maximum -> prevent overflow
        exp_values = np.exp(inputs) - np.max(inputs, axis=1, keepdims=True)
        norm = np.sum(exp_values, axis=1, keepdims=True)
        prob_dist = exp_values / norm
        self.output = prob_dist

    def backward(self, der):
        self.dinputs = np.empty_like(der)

        for i, (single_output, single_der) in enumerate(zip(self.output, der)):
            single_output = single_output.reshape(-1, 1)

            jacobian = np.diagflat(single_output) - np.dot(
                single_output, single_output.T
            )

            self.dinputs[i] = np.dot(jacobian, single_der)


class SGD:
    def __init__(self, lr=0.01):
        self.lr = lr

    def update(self, layer):
        layer.weights -= self.lr * layer.dweights
        layer.biases -= self.lr * layer.dbiases


def get_batches(X, y, batch_size):
    num_samples = X.shape[0]
    indices = np.arange(num_samples)
    np.random.shuffle(indices)
    for start in range(0, num_samples, batch_size):
        end = min(start + batch_size, num_samples)
        batch_indices = indices[start:end]
        yield X[batch_indices], y[batch_indices]



def preprocess_data(X, y):
    X = (X.reshape(X.shape[0], -1) / 255.0)  # Flatten and scale pixel values to [0, 1]
    y = np.eye(10)[y]  # One-hot encoding for target labels
    return X, y


(X_train, y_train), (X_test, y_test) = tf.keras.datasets.mnist.load_data()
X_train, y_train = preprocess_data(X_train, y_train)
X_test, y_test = preprocess_data(X_test, y_test)

# Model
d1 = Dense_Layer(784, 64)
a1 = ReLU()
d2 = Dense_Layer(64, 10)
softmax_output = Softmax()

# Hyps
loss_func = Cat_Cross_Ent_Back()
lr = 0.1
opt = SGD(lr)
epochs = 10

batch_size = 30

# Training loop
for epoch in range(epochs):
    total_loss = 0
    total_acc = 0
    num_batches = 0

    for X_batch, y_batch in get_batches(X_train, y_train, batch_size):
        # FORWARD PASS
        d1.forward(X_batch)
        a1.activate(d1.output)
        d2.forward(a1.output)
        loss = loss_func.forward(d2.output, y_batch)
        preds = np.argmax(loss_func.output, axis=1)
        y_batch_labels = np.argmax(y_batch, axis=1)
        acc = np.mean(preds == y_batch_labels)

        total_loss += loss
        total_acc += acc
        num_batches += 1

        # BACK PASS
        loss_func.backward(loss_func.output, y_batch)
        d2.backward(loss_func.dinputs)
        a1.backward(d2.dinputs)
        d1.backward(a1.dinputs)

        opt.update(d1)
        opt.update(d2)

    avg_loss = total_loss / num_batches
    avg_acc = total_acc / num_batches

    if epoch % 1 == 0:
        print("EPOCH: {}, AVG LOSS: {}, AVG ACC: {}".format(epoch, avg_loss, avg_acc))

d1.forward(X_test)
a1.activate(d1.output)
d2.forward(a1.output)
test_loss = loss_func.forward(d2.output, y_test)
test_preds = np.argmax(loss_func.output, axis=1)
test_labels = np.argmax(y_test, axis=1)
test_acc = np.mean(test_preds == test_labels)
print("Test Loss: {}, Test Accuracy: {}".format(test_loss, test_acc))
