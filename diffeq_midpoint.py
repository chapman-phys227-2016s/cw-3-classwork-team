#! /usr/bin/env python

"""
File: diffeq_midpoint.py

Copyright (c) 2016 Taylor Patti

License: MIT

This module uses a difference equation to take the integral via
summation over the midpoints by using numpy vectorization techniques.

"""

import numpy as np

def vector_midpoint(f, a, b, n=100):
    """Uses vectors to create an integral array, containing
    all of the values of integrals for each subsegment."""
    indexer = range(n+1)
    x = np.linspace(a, b, n+1)
    sum_vec = np.zeros_like(x)
    sum_vec[0] = 0
    h = (b - a) / float(n)
    
    for i in indexer[1:]:
        sum_vec[i] = sum_vec[i-1] + f(a + h/float(2) + i*h)
    sum_vec = sum_vec * h
    return x, sum_vec

def test_integral_value():
    """Tests the integral function by checking for exact match with
    symbolic integration methods."""
    
    def test_function(t):
        return 5*t + 2
    
    def exact_integral(x, a):
        return ((5*x**2) / float(2)) + 2*x - (((5*a**2) / float(2)) + 2*a)
    
    a = 5
    x, f = vector_midpoint(test_function, 5, 12, n=1000000)
    apt = np.allclose(f, exact_integral(x, a))
    msg = "Integrals do not match."
    print f
    print exact_integral(x, a)
    assert apt, msg