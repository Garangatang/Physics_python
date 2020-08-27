import matplotlib
matplotlib.use('Agg')
import numpy as np
import pylab as pl
from numpy.random import choice

N = 25
[S,C,R] = [0.,1.,2.]
n = 24
x = np.zeros(N)

x[0] = 1
print(x)
#For loop to iterate infection over time

def infection(arr):
        for delta_t in range(n):

#       N = 25
#       x = np.zeros(N)
#       x[0] = 1
        #For loop to select samples of n size out of x
                samp = np.random.choice(a = arr, size = 5, replace = True)
                print(samp)
                if 1. in samp:
                        print('Infection')
                        for i in range(5):
                                if  samp[i] == 0.:
                                        if np.random.uniform(0,1) < .1:
                                                samp[i] = 1.
                                                np.append(arr,samp)
                                                print('1:',samp)
                                        continue
                                else:
                                        samp[i] = 2.
                                        np.append(arr,samp)
                                        print('2:',samp)

                else:
                        continue

        return arr

print(infection(x))

def no_replace(arr):
        for delta_t in range(n):
                np.random.choice(a = arr, size = 5, replace = False)
        return arr

print(no_replace(x))
