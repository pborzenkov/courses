#!/usr/bin/env python2

import math
import numpy as np
import scipy.optimize
import matplotlib.pyplot as plt

def f(x):
    x = float(x)
    return math.sin(x / 5) * math.exp(x / 10) + 5 * math.exp(-x / 2)

def h(x):
    return int(f(x))
vf = np.vectorize(h)

x = np.arange(1, 30, 0.1)

min1 = scipy.optimize.minimize(h, 30, method='BFGS')
print "Minimum found by BFGS"
print min1
print

min2 = scipy.optimize.differential_evolution(h, [(1, 30)])
print "Minimum found by differential evolution"
print min2
print

plt.plot(x, vf(x), min1.x, vf(min1.x), 'ro', min2.x, vf(min2.x), 'go')
plt.show()
