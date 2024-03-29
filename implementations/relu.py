#Implementation of the relu function in python

import numpy as np
import matplotlib.pyplot as plt

def relu(num):
    return np.maximum(num, 0)

num_seq = np.linspace(-5, 5, 100)   # 'np.linspace' creates evenly spaced numbers in sequences structured as a numpy array
plt.plot(num_seq, relu(num_seq),'b') # the 'b'-parameter for 'blue'. Choose 'g' for 'green' or 'r' for 'red', etc.

plt.xlabel('x')
plt.ylabel('y')

plt.title('relu function')
plt.grid()

plt.show()



