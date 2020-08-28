#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np
x, y = np.loadtxt('init.dat', unpack = True, usecols = [0,1])
plt.ylabel('y numbers')
plt.xlabel('x numbers')
plt.xlim(16)
plt.ylim(16)
plt.title('My Initial')

plt.plot(x, y, '-b')

#plt.show()
plt.savefig('filename.png')
