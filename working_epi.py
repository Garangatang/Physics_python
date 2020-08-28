import numpy as np
import pylab as pl
from numpy import random

N = 100
[S,C,R] = [0,1,2]

prob = .33

x = np.zeros(N)
x[0] = 1
print(x)
def infection(arr):
        print(arr)
        while (np.sum(x == C)):
                for i in range(N):
                        if x[i] == C:
                                x[i] = 2
                                jarray = np.random.randint(0,N,4)
                                print(jarray)
                                for j in jarray:
                                        if x[j] == S:
                                                if np.random.uniform(0,1) < prob:
                                                        x[j] = C
        return arr, np.unique(arr, return_counts = True)

print(infection(x))
