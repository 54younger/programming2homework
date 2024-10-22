
"""
Solutions to module 4
Review date:
"""

student = ""
reviewer = ""

import math as m
import random as r

import concurrent.futures as future
import multiprocessing as mp
from functools import reduce

from MA4_1_2 import sphere_volume, hypersphere_exact

def loop_sv(n, d, np):
    results = []
    for _ in range(np):
        results.append(sphere_volume(n,d))
    return sum(results) / np

# parallel code - parallelize for loop
def sphere_volume_parallel1(n,d,np):
    #using multiprocessor to perform 10 iterations of volume function
    
    batch_size = n
    with future.ProcessPoolExecutor() as ex:
        results = ex.map(sphere_volume, [batch_size]*np, [d]*np) 
    ave_result = sum(results) / np
    #print(ave_result)
    return ave_result

# parallel code - parallelize actual computations by splitting data
def sphere_volume_parallel2(n, d, np):

    batch_size = n // np
    with future.ProcessPoolExecutor() as ex:
        results = list(ex.map(sphere_volume, [batch_size]*np, [d]*np))
    #print(results)
    ave_result = sum(results) / np
    #print(ave_result)
    return ave_result

def main():
    # part 1 -- parallelization of a for loop among 10 processes 
    n = 100000
    d = 11

    for y in range (10):
        #sphere_volume(n,d)
        pass
    
    sphere_volume_parallel1(n,d,8)
    sphere_volume_parallel2(n,d,8)


if __name__ == '__main__':
	main()
