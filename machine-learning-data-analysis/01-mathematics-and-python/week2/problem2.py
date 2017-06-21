#!/usr/bin/env python

import math
import numpy
import scipy.linalg
import matplotlib.pyplot as plt

def f(x):
    x = float(x)
    return (math.sin(x / 5.)) * math.exp(x / 10.) + 5 * math.exp(-x / 2.)

def fw(w, x):
    x = float(x)
    out = 0.
    power = 0
    for wi in w:
        out += wi * x**power
        power += 1
    return out

x = numpy.arange(1, 16, 0.5)
fx = [f(xi) for xi in x]

m1 = numpy.array([[1., 1.], [1., 15.]])
w1 = scipy.linalg.solve(m1, [f(1.), f(15.)])
fxw1 = [fw(w1, xi) for xi in x]

m2 = numpy.array([[1., 1., 1.], [1., 8., 64.], [1., 15., 225.]])
w2 = scipy.linalg.solve(m2, [f(1.), f(8.), f(15.)])
fxw2 = [fw(w2, xi) for xi in x]

m3 = numpy.array([[1., 1., 1., 1.], [1., 4., 16., 64.], [1., 10., 100., 1000.], [1., 15., 225., 3375.]])
w3 = scipy.linalg.solve(m3, [f(1.), f(4.), f(10.), f(15.)])
fxw3 = [fw(w3, xi) for xi in x]
print w3

plt.plot(x, fx, x, fxw1, x, fxw2, x, fxw3)
plt.show()
