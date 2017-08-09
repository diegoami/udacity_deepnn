"""Softmax."""


import numpy as np


x =  1000000000
for _ in range(1000000):
    x += 0.000001
x -= 1000000000
print(x)
