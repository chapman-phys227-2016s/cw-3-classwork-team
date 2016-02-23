#! /usr/bin/env python

"""
File: boundary_layer_func1.py
Copyright (c) 2016 Chinmai Raman
License: MIT

Course: PHYS227
Assignment: 5.49
Date: Feb 18, 2016
Email: raman105@mail.chapman.edu
Name: Chinmai Raman
Description: Calculates an exponential function and returns the numerator, denominator and the fraction as a 3-tuple.
"""

import numpy as np
import math

def v(x, mu = 1e-6, exp = math.exp):
    num = 1.0 - exp(x / mu)
    den = 1.0 - exp(1.0 / mu)
    return num, den, num / den

def part_b():
    x = np.linspace(0,1,11)
    print('part b (using default float64):')
    for i in x:
        try:
            print v(i, 1e-3, np.exp)
        except:
            print("overflow")

def part_d():
    x0 = np.linspace(0,1,11)
    x = np.float128(x0)
    mu = np.float128(1e-3)
    print('part d (using float128):')
    for i in x:
        try:
            print v(i, mu, np.exp)
        except:
            print("overflow")

def part_e():
    x0 = np.linspace(0,1,11)
    x = np.float32(x0)
    mu = np.float32(1e-3)
    print('part e (using float32):')
    for i in x:
        try:
            print v(i, mu, np.exp)
        except:
            print("overflow")

def test_v():
    assert (abs(v(1, 1)[2] - 1.0) < 1e-3), "Failure"

test_v()

part_b()
part_d()
part_e()