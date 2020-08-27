import numpy as np
import pylab as pl
from numpy import random

N = 10
n=500
[S,C,AR,V,R,D] = [0,1,2,3,4,5]


prob_death = .2
prob_rec = .80
prob_inf = .2
pop = np.zeros(N)
pop[0] = 1
#np.random.seed(193)
init_arr = np.array([0,1,2,3])
#Set array with given weights based upon above statistics
arr = np.random.choice(init_arr,size =n, p = [0.3,0.1,0.3,0.3])
#arr = np.zeros(n)
#arr[0] = 1
#Plug in weighted array and perform infection on it, randomly selecting rows
def infection(pop_maker):
        #print(pop_maker,np.unique(pop_maker, return_counts = True))
        while (np.sum(arr == C)):
                for i in range(n):
                        if arr[i] == C:
                                #print(arr[i])
                                if np.random.uniform(0,1) < prob_rec:
                                    arr[i] = R
                                pop_r = np.arange(i-10,i, 1)
                                #pop_r = np.random.randint(0,N,6) #gives random positions to assign to array pop
                                #print(pop_r)
                                for p in pop_r:
                                    #print(arr[p])
                                    if arr[p] == S:
                                        if np.random.uniform(0,1) < prob_inf:
                                            arr[p] = C
                                    elif arr[p] == AR:
                                        if np.random.uniform(0,1) < prob_death:
                                            arr[p] = D

        return pop_maker, np.unique(pop_maker, return_counts = True)

#print(pop_maker(n,init_arr))
#print(pop_maker(n,init_arr))
print('===========================')
print(infection(arr))
#coin flip
"""
#!/usr/plocal/bin/python3
import numpy as np
import sys

print('Enter the number of coin flips wanted: ',end='')
userinput = input()
n = int(sys.argv[1])

print(np.random.randint(0,2,n))
"""
#coin prob
"""
import numpy as np
#heads is = 1, tails is = 0
n = 10
ntrials = 10000
matr = np.random.randint(0,2,(ntrials,n))
print(matr)
arr = np.sum(matr, axis = 1)
print(arr)
z = np.where(arr==9)
x = np.size(z)

print((x/ntrials)*100)
"""
