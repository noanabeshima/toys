# bernstein.py

'''
Bernstein polynomial visualizer
'''

import operator as op
from functools import reduce
from sympy import *
import numpy as np
import matplotlib.pyplot as plt
from time import sleep

x = symbols('x')


# Parameters
#-----------------------------------

# f(x) in symbolic form
f = 20*(x-.5)**3+10*x*sin(2*2*pi*x)
#f = (5*(x-.5))**5+20*(5*(x-.5))**2

RENDER_BASIS = True
N = 100
MANUAL_NEXT_ENTRY = False

#-----------------------------------


f_str = str(f)
f = lambdify(x, f)

def choose(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer / denom

def basis(n, k):
    return choose(n, k)*(x**k)*(1-x)**(n-k)

def weighted_basis(f, n, k):
    return f(k/n)*basis(n, k)


def bernstein_with_basis(f, n):
    # returns bernstein polynomial in range 0 to 1
    if isinstance(f, Expr): # i.e. sympy.Expr
        f = lambdify(x, f)
    result = 0
    basis_funcs = []
    temp = []
    for k in range(n+1):
        b = weighted_basis(f, n, k)
        result += b
        basis_funcs.append(lambdify(x, b))
    return lambdify(x, result), basis_funcs

# Change figure size
plt.figure(figsize=(20,10))

# Rendering
plt.ion()
ax = plt.gca()
x_axis = np.arange(0,1,.01)

for n in range(1, N+1):
    plt.clf()
    plt.text(.05,.94, 'N = '+str(n), horizontalalignment='center', verticalalignment='center', \
             transform=ax.transAxes, fontsize=20, \
             bbox=dict(facecolor='red', alpha=0.5))
    plt.title(f_str, fontsize=15)

    g, basis_funcs = bernstein_with_basis(f, n)

    if RENDER_BASIS:
        for k in range(1,n+1):
            plt.plot(x_axis, list(map(basis_funcs[k], x_axis)), c=(.153, .023, .545, np.clip(.2*np.random.randn()+.5, a_min = 0, a_max = 1)))

    plt.plot(x_axis, list(map(g, x_axis)), c='b')
    plt.plot(x_axis, f(x_axis), c = 'r')
    plt.pause(.01)
    if MANUAL_NEXT_ENTRY:
        plt.waitforbuttonpress(0)


plt.waitforbuttonpress(0)
plt.close()
