# -*- coding: utf-8 -*-
from __future__ import unicode_literals
def fib(n):
    a = 1
    b = 0
    for i in range(n):
        a = b
        b = a+b
    return b

def fi(n):
    return fib(n) / fib(n - 1)

print('φ =', fi(100))


# from math import sqrt

# fi = 1.618033988749895

# def fib(n):
#     return (fi ** n - (1 - fi) ** n) / sqrt(5)

# for i in range(16):
#     print("fib({0}) = {1}".format(i, fib(i)))