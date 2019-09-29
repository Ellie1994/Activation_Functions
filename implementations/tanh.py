#Implementation of the tanH function in python

import numpy as np
import matplotlib.pyplot as plt

def tanH(num):
    return (2 / (1 + np.exp(-2*num))) - 1

num_seq = np.linspace(-5, 5, 100)   # 'np.linspace' creates evenly spaced numbers in sequences structured as a numpy array
plt.plot(num_seq, tanH(num_seq),'g') # the 'r'-parameter for 'red. Chose 'g' for 'green' or 'b' for 'blue', etc.

plt.xlabel('x')
plt.ylabel('y')

plt.title('tanH function')
plt.grid()

plt.show()



