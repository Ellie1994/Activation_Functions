#Implementation of the sigmoid function in python

import numpy as np
import matplotlib.pyplot as plt

def sigmoid(num):
    return 1 / (1 + np.exp(-num))

num_seq = np.linspace(-5, 5, 100)   # 'np.linspace' creates evenly spaced numbers in sequences structured as a numpy array
plt.plot(num_seq, sigmoid(num_seq),'r') # the 'r'-parameter for 'red. Chose 'g' for 'green' or 'b' for 'blue', etc.

plt.xlabel('x')
plt.ylabel('y')

plt.title('sigmoid function')
plt.grid()

plt.show()



