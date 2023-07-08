#
# Just toy model using TG
#

!git clone https://github.com/geohot/tinygrad.git
cd tinygrad/
!python3 -m pip install -e .

import time
import numpy as np
from tinygrad.tensor import Tensor
from tinygrad.nn import optim
import tinygrad.nn as nn
from tinygrad.helpers import flatten
from tinygrad.nn.optim import SGD
from sklearn.datasets import fetch_openml

X, y = fetch_openml('mnist_784', version=1, return_X_y=True, as_frame=False, )
print(X.shape, y.shape)

# from tinygrad.nn import Linear

class TinyNet:
  def __init__(self):
    self.l1 = nn.Linear(784, 128, bias=False)
    self.l2 = nn.Linear(128, 10, bias=False)

  def __call__(self, x):
    x = self.l1(x)
    x = x.leakyrelu()
    x = self.l2(x)
    return x.log_softmax()

net = TinyNet()

Tensor.training = True

# from extra.training import sparse_categorical_crossentropy
def cross_entropy(out, Y):
  num_classes = out.shape[-1]
  YY = Y.flatten().astype(np.int32)
  y = np.zeros((YY.shape[0], num_classes), np.float32)
  y[range(y.shape[0]),YY] = -1.0*num_classes
  y = y.reshape(list(Y.shape)+[num_classes])
  y = Tensor(y)
  return out.mul(y).mean()

# from tinygrad.nn.optim import SGD
opt = SGD([net.l1.weight, net.l2.weight], lr=0.01)

num_epochs = 4000

weight_bias_dictionary = {}
running_loss, correct, total = 0.0, 0.0, 0.0
for epoch in range(num_epochs):
    weigth_bias = {}
    start_time = time.time()

    samp = np.random.randint(0, X.shape[0], size=(64))
    batch = Tensor(X[samp].astype('float32') / 255.0, requires_grad=False)
    labels = y[samp]
    
	# Forward pass
    out = net(batch)
    # Compute loss
    loss = cross_entropy(out, labels)
    
	opt.zero_grad()
    loss.backward()

    # Update parameters
    opt.step()

    # Calculate accuracy
    pred = np.argmax(out.numpy(), axis=-1)
    labels = [eval(label) for label in labels]

    acc = (pred == labels).mean()
    if epoch % 100 == 0:
      print(f"Time Taken: {time.time()-start_time:.3f}s, Epoch [{epoch+1}/{num_epochs}], Loss: {loss.numpy():.5f}, Accuracy: {acc:.5f}")

# set training flag to false
Tensor.training = False

st = time.perf_counter()
avg_acc = 0
for step in range(1000):
  # random sample a batch
  samp = np.random.randint(0, X.shape[0], size=(64))
  batch = Tensor((X[samp].astype('float32') / 255.0), requires_grad=False)
  # get the corresponding labels
  labels = y[samp]

  # forward pass
  out = net(batch)

  # calculate accuracy
  pred = np.argmax(out.numpy(), axis=-1)

  labels = [eval(label) for label in labels]
  avg_acc += (pred == labels).mean()

print(f"Test Accuracy: {avg_acc / 1000}")
print(f"Time Taken To Test: {time.perf_counter() - st}")
