
"""
Solutions to module 4
Review date:
"""

student = ""
reviewer = ""

import math as m
import random as r
import numpy as np
from functools import reduce
import time
def sphere_volume(n, d):
    # n is a list of set of coordinates
    # d is the number of dimensions of the sphere
    np.random.seed(int(time.time()))
    radius = 1
    dots = []
    for dot in range(n):
        coordinates = np.random.uniform(-radius, radius, d)
        dot = sum(map(lambda x: x**2, coordinates))
        dots.append(dot)
    count = len(list(filter(lambda x: x<=radius, dots)))
    volume = count / n * (m.pow(2*radius, d))
    #print(volume)
    return volume

def hypersphere_exact(n,d):
    radius = 1
    volume_pi = m.pi**(d/2) / m.gamma(d/2 + 1) * radius**d
    #print(volume_pi)
    return volume_pi
    
def main():
    n = 100000
    d = 2
    sphere_volume(n,d)
    hypersphere_exact(n,d)

if __name__ == '__main__':
	main()
