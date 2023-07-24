"""
This code builds a small NN,
it can do a forward pass, it can
also do a backward pass. This
model has SGD avalible.


Has a custom data loader, just pass it 
a number of points per class, and set the
class in the code. Will generate j points
per n classes in Euclidean space.

the data points will be plotted for visual.

During training the model will display
the prediction, GT, and then the tensor
showing the prob dist P: --> [0, 1].

The loss and acc curves will be plotted after
training too.

SGD now has a very stupid LR sched.

Data can now be generated with a noise factor
producing a tougher to classify euclidean space.
"""
import numpy as np
from tqdm import tqdm
import dataset
import random
import matplotlib.pyplot as plt

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
        exp_values = np.exp(inputs - np.max(inputs, axis=1, keepdims=True))
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
    def __init__(self, lr = 0.01, decay = 0.0001):
        self.lr = lr
        self.iter = 0
        self.decay = decay
    
    def update(self, layer):
        #if (self.iter % 10_000 == 0):
        #    self.lr = self.lr * self.decay
        #    print('lr: ', self.lr)
        
        layer.weights -= self.lr * layer.dweights
        layer.biases -= self.lr * layer.dbiases
        
        #self.iter += 1

def get_batches(X, y, batch_size):
    num_samples = X.shape[0]
    indices = np.arange(num_samples)
    np.random.shuffle(indices)
    for start in range(0, num_samples, batch_size):
        end = min(start + batch_size, num_samples)
        batch_indices = indices[start:end]
        yield X[batch_indices], y[batch_indices]

def preprocess_data(X, y):
    classes = 5
    X = (X.reshape(X.shape[0], -1) / 255.0) 
    
    # One-hot encoding for target labels
    y = np.eye(classes)[y]
    return X, y

def plot_graph(loss_values, accuracy_values):
    # Plot the loss curve
    plt.figure(figsize=(8, 6))
    plt.plot(range(len(loss_values)), loss_values, label='Loss')
    plt.title("Loss Curve")
    plt.xlabel("Epoch")
    plt.ylabel("Loss")
    plt.legend()
    plt.grid(True)
    plt.show()

    # Plot the accuracy curve
    plt.figure(figsize=(8, 6))
    plt.plot(range(len(accuracy_values)), accuracy_values, label='Accuracy')
    plt.title("Accuracy Curve")
    plt.xlabel("Epoch")
    plt.ylabel("Accuracy")
    plt.legend()
    plt.grid(True)
    plt.show()

# DataSet
# Noise will load the data in a certain way
# high 3+ will produce very scattered points
# low <= will produce more segregated clusters
X, y = dataset.dataset_gen(points_per_class = 500, noise = 3)

# Plot
num_classes = len(np.unique(y))
class_colors = plt.cm.coolwarm(np.linspace(0, 1, num_classes))

plt.figure(figsize=(8, 6))
for class_index in range(num_classes):
    class_mask = (y == class_index)
    plt.scatter(X[class_mask, 0], X[class_mask, 1], color=class_colors[class_index], label=f"Class {class_index}")
plt.legend()
plt.grid(True)
plt.show()

# Model
d1 = Dense_Layer(2, 128)
a1 = ReLU()
d2 = Dense_Layer(128, 5)

# Hyps
loss_func = Cat_Cross_Ent_Back()
lr = 0.1
decay = 0.01
opt = SGD(lr, decay)
epochs = 10_000
y_copy = y.copy()

loss_values = []
accuracy_values = []

for epoch in tqdm(range(epochs), desc="Training"):
    # FORWARD PASS
    d1.forward(X)
    a1.activate(d1.output)
    d2.forward(a1.output)
    loss = loss_func.forward(d2.output, y)
    preds = np.argmax(loss_func.output, axis=1)
    
    if len(y.shape) == 2:
        y = np.argmax(y, axis=1)
    
    acc = np.mean(preds == y)

    if epoch % 100 == 0:
        print("\nEPOCH: {}\nLOSS: {}\nACC: {}".format(epoch, loss, acc))
        random_idx = random.randint(0, len(X) - 1 )
        random_prediction = np.round(loss_func.output[random_idx], 2)
        gt = y_copy[random_idx]
        print("Random Data Point: {}".format(random_idx))
        print("Ground Truth Label: {}".format(gt))
        print("Predicted Label: {}".format(preds[random_idx]))
        print("Prediction Distribution for Data Point {}:".format(random_idx))
        print(random_prediction)
        print('\n') 
    
	# BACK PASS
    loss_func.backward(loss_func.output, y)
    d2.backward(loss_func.dinputs)
    a1.backward(d2.dinputs)
    d1.backward(a1.dinputs)
    
    # Opt step
    opt.update(d1)
    opt.update(d2)

    loss_values.append(loss)
    accuracy_values.append(acc)

plot_graph(loss_values, accuracy_values)
