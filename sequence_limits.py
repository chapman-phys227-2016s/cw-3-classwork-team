#! /usr/bin/env python

"""
File: sequence_limits.py
Copyright (c) 2016 Austin Ayers
License: MIT

Course: PHYS227
Assignment: A. 1
Date: Feb 11, 2016
Email: ayers111@mail.chapman.edu
Name: Austin Ayers
Description: Determines the limit of a sequence
"""
import numpy as np
import matplotlib.pyplot as plt

def seq_a(n):
    """
    Returns an element in a sequence given the n value
    """
    return ((7.0+(1.0/(float(n)+1.0)))/(3.0-(1.0/(float(n)+1.0)**2)))

def seq_c(n):
    return np.sin(2.0**(-1 *float(n)))/(2.0**(-1 *float(n)))

def part_a():
    """
    Writes out the sequence for N = 100, and finds the value as n -> inf
    """
    sequence = []
    for i in range(0,100,2):
        print i
        print seq_a(i)
        sequence.append(seq_a(i))
    print "\n\n"
    print "The series converges to: 7/3 or 2.3333..., and a_N was: " + str(seq_a(100)) + " and the difference was: " + str((seq_a(100)-2.33333333333333333))
    return sequence

def limit(seq):
    """
    Determines if a series has a limit and returns it, if the series has no limit it outputs None
    """
    cond = True
    for i in range(1,len(seq)-1):
        if not (abs(seq[i]) - abs(seq[i+1]) < abs(seq[i-1]) - abs(seq[i])):
            print "None"
            cond = False
            break
    if(cond):
        print "The limit exists (to this algorithm's knowledge)"
    if(seq[-1] - seq[-2] < 0.01):
        return seq[-1]

def part_b():
    """
    tests limit(seq) if it works for the sequence in part a
    """
    seq_a = part_a()
    print "The limit is roughly: " + str(limit(seq_a))

def part_c():
    """
    tests limit(seq) if it works for the sequence in part c
    """
    sequence = []
    for i in range(500):
        sequence.append(seq_c(i))
    print "The limit is roughly: " + str(limit(sequence))
def sin_x(x):
    return np.sin(x)
def D(f, x, N):
    """
    takes a function f(x), a value x, and the number N and returns the sequence for 0,N
    """
    sequence = []
    for i in range(N):
        sequence.append((f(float(x)+(2.0**(-1 *float(i))))-f(x))/(2.0**(-1 *float(i))))
    return sequence

def part_d():
    seq_d = D(sin_x, 0, 80)
    print str(limit(seq_d))
    print "notice this fails because the function is oscillatory in behavior (sin(x))"
    plt.plot(range(80), seq_d, 'go')
    plt.show

def part_e():
    seq_e = D(sin_x, np.pi, 80)
    print str(limit(seq_e))
    plt.plot(range(80), seq_e, 'go')
    plt.show

def part_f():
    print "the computations for x = pi go wrong for large N because sin(pi) = 0 and 2 ** (-n) approaches 0 as well, so the numerator and denominator both go to 0 and that usually leads to problems."

def run():
    """
    Runs the entire program with parts
    """
    print "Part (a): "
    part_a()
    print
    print "Part (b): "
    part_b()
    print
    print "Part (c): "
    print
    part_c()
    print "Part (d): "
    print
    part_d()
    print "Part (e): "
    print
    part_e()
    print "Part (f): "
    print
    part_f()
    print "Finished"