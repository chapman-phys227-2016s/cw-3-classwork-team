#!/usr/bin/python

import numpy

def pi_sequence(n, f):
    """
    Returns a numpy array of length n, with each value being the summed output
    of function f at the point i (its index)
    """
    output = numpy.zeros(n)
    for i in range(1, n):
        output[i] = output[i-1] + f(i)
    return output

def fa(x):
    return 4 * (-1) ** (x + 1) / float(2*x -1)

def fb(x):
    """
    In order to be a pi converging sequence, each element must be ^ .5
    """
    return 6 * x ** -2

def fc(x):
    """
    In order to be a pi converging sequence, each element must be ^ .25
    """
    return 90 * x ** -4

def fd(x):
    return (6 / float(3 ** .5)) * (-1) ** (x - 1) / float(3 ** (x - 1) * (2*x - 1 ))

def fe(x):
    return 16 * (-1) ** (x - 1) / float(5 ** (2*x - 1) * (2*x - 1) ) - 4 * (-1) ** (x - 1) / float(239 ** (2*x - 1) * (2*x - 1) )

