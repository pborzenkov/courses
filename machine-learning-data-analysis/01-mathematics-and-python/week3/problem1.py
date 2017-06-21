#!/usr/bin/env python2

import math
import numpy as np
import scipy.optimize
import matplotlib.pyplot as plt

def f(x):
    x = float(x)
    return math.sin(x / 5) * math.exp(x / 10) + 5 * math.exp(-x / 2)
vf = np.vectorize(f)

x = np.arange(1, 30, 0.1)

min1 = scipy.optimize.minimize(f, 2, method='BFGS')
print "Minimum with initial value 2"
print min1
print

min2 = scipy.optimize.minimize(f, 30, method='BFGS')
print "Minimum with initial value 30"
print min2
print

plt.plot(x, vf(x), min1.x, vf(min1.x), 'ro', min2.x, vf(min2.x), 'go')
plt.show()
