"""
Solutions to module 1
Student: 
Mail:
Reviewed by:
Reviewed date:
"""

"""
Important notes: 
These examples are intended to practice RECURSIVE thinking. Thus, you may NOT 
use any loops nor built in functions like count, reverse, zip, math.pow etc. 

You may NOT use any global variables.

You can write code in the main function that demonstrates your solutions.
If you have testcode running at the top level (i.e. outside the main function)
you have to remove it before uploading your code into Studium!
Also remove all trace and debugging printouts!

You may not import any packages other than time and math and these may
only be used in the analysis of the fib function.

In the oral presentation you must be prepared to explain your code and make smalleror 
modifications.

We have used type hints in the code below (see 
https://docs.python.org/3/library/typing.html).
Type hints serve as documatation and and doesn't affect the execution at all. 
If your Python doesn't allow type hints you should update to a more modern version!

"""




import time
import math

def multiply(m: int, n: int) -> int:  
    """ Computes m*n using additions"""
    smaller = min(m,n)
    larger = max(m,n)
    
    if smaller > 1:
        return larger + multiply(smaller-1, larger)
    elif smaller == 0:
        return 0
    else:
        return larger



def harmonic(n: int) -> float:              
    """ Computes and returns the harmonc sum 1 + 1/2 + 1/3 + ... + 1/n"""
    if (n):
        return 1/n + harmonic(n-1)
    else:
        return n

def get_binary(x: int) -> str:              
    """ Returns the binary representation of x """
    if x >= 0:
        if x>1:
            return get_binary(x//2) + str(x%2)
        elif x==1:
            return "1"
        else:
            return "0"
    else:
        if x==-1:
            return "-1"
        else:
            return get_binary(math.ceil(x/2)) + str(x%2)


def reverse_string(s: str) -> str:        
    """ Returns the s reversed """
    if len(s)<=1:
        return s
    else:
        return s[-1] + reverse_string(s[:-1])

def largest(a: iter):
    """ Returns the largest element in a"""
    if len(a) > 1:
        max_of_rest = largest(a[1:])
        return a[0] if a[0] > max_of_rest else max_of_rest
    else:
        return a[0]

def count(x, s: list) -> int:
    """ Counts the number of occurrences of x on all levels in s"""
    if not s:
        return 0
    times = 1 if s[0] == x else 0
    if isinstance(s[0], list):
        times += count(x, s[0])
    return times + count(x, s[1:])



def bricklek(f: str, t: str, h: str, n: int) -> str:  
    """ Returns a string of instruction ow to move the tiles """
    if n == 0:
        return []
    else:
        return (bricklek(f, h, t, n-1) + [f + '->' + t] + bricklek(h, t, f, n-1))


def fib(n: int) -> int:                      
    """ Returns the n:th Fibonacci number """
    # You should verify that the time for this function grows approximately as
    # Theta(1.618^n) and also estimate how long time the call fib(100) would take.
    # The time estimate for fib(100) should be in reasonable units (most certainly
    # years) and, since it is just an estimate, with no more than two digits precision.
    #
    # Put your code at the end of the main function below!
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def fib_mem(n, memory = None):
    if memory is None:
        memory = {0: 0, 1: 1}
    if n not in memory:
        memory[n] = fib_mem(n-1, memory) + fib_mem(n-2, memory)
    return memory[n]
    
def main():
    print('\nCode that demonstates my implementations\n')

    print('\n\nCode for analysing fib and fib_mem\n')
    time_list=[]
    theta_list=[]
    for i in range(0,32):
        start_t = time.perf_counter()
        #fib_mem(i)
        fib(i)
        end_t = time.perf_counter()
        time_list.append(end_t-start_t)
        theta_list.append(math.pow(1.618, i))
        print(f"when n={i}, the running time of fib is {time_list[i]:.2f}, the estimate theta is {theta_list[i]:.2f}\n" 
              f"the time ratio is {(time_list[i]/theta_list[i]*pow(10,6)):.2f} * 10^6\n")
    time_100 = sum(time_list) / sum(theta_list) * math.pow(1.618, 100) / (60*60*24*365)
    time_50 = sum(time_list) / sum(theta_list) * math.pow(1.618, 50) / (60*60)
    print(f"the estimate time of fib(100) is {time_100:.2f} years\n"
          f"the estimate time of fib(50) is {time_50:.2f} hours\n")

    print('\nBye!')


    
if __name__ == "__main__":
    main()

####################################################

"""
  Answers to the none-coding tasks
  ================================
  
  
  Exercise 8: Time for the tile game with 50 tiles:
    t(50)=2^50-1=1125899906842623 moves
    

  
  
  
  Exercise 9: Time for Fibonacci:
    the estimate time of fib(100) is 17617539.37 years
    the estimate time of fib(50) is 5.49 hours
    (using time.time())

    the estimate time of fib(100) is 17812885.63 years
    the estimate time of fib(50) is 5.55 hours
    (using time.perf_counter())
  
  
  Exercise 10: Time for fib_mem:
  
    the estimate time of fib_mem(100) is 462.60 years
  
  
  
  Exercise 11: Comparison sorting methods:
  insertion sort:
    10^6: 1000^2s = 11.574days
    10^9: 1000000^2 = 11574000days = 3170.97years
  merge sort:
    10^6: 1000n*log(1000n)  = 1000s
    10^9: 1000000s = 277h
  
  
  
  
  Exercise 12: Comparison Theta(n) and Theta(n log n)
    c=0.1
    n <= 0.1n*logn
    logn >= 10
    n >= 10^10
  
  
"""
