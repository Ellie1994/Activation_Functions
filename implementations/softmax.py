#Implementation of the softmax function in python

import numpy as np
import matplotlib.pyplot as plt

def softmax(num):
    return np.exp(num) / np.sum(np.exp(num), axis=0)
    
    # Axes are needed for multi-dimensional arrays. 
    # A 2-dimensional array, for example, has two axes (x,y): the first one (y) is vertical and goes downwards across the rows (axis 0). 
    # The second one is horizontal and goes across columns (axis 1).

num_seq = np.linspace(-5, 5, 100)   # 'np.linspace' creates evenly spaced numbers in sequences structured as a numpy array
plt.plot(num_seq, softmax(num_seq),'m') # the 'm'-parameter for 'magenta'. Choose 'r' for 'red' or 'b' for 'blue', etc.

plt.xlabel('x')
plt.ylabel('y')

plt.title('softmax function')
plt.grid()

plt.show()
