"""
Solutions to module VA 4

Student: Chenyang Wang
Mail: chenyang.wang.6882@student.uu.se
"""
#!/usr/bin/env python3
import time
import matplotlib.pyplot as plt
from person import Person
"""
Write a script that gives a plot for comparison of two approaches for Fibonacci numbers
"""
def fib_py(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fib_py(n-1) + fib_py(n-2)

def count_time_py(func, *args):

	start = time.time()
	
	func(*args)
	end = time.time()
	print(f'{func.__name__} takes {end - start} seconds to run')
	return end - start

def count_time_cpp(n):
	person = Person(n)
	start = time.time()
	person.fib()
	end = time.time()
	print(f'fib_cpp takes {end - start} seconds to run')
	return end - start

def main():
	py_time = []
	cpp_time = []
	for n in range(30, 45):
		#py_time.append(count_time_py(fib_py, n))
		cpp_time.append(count_time_cpp(n))
	#plt.plot(range(30, 45), py_time, label='Python')
	plt.plot(range(30, 45), cpp_time, label='C++')
	plt.legend()
	plt.xlabel('n')
	plt.ylabel('time')
	plt.savefig('fib_cpp.png')
	plt.show()
	
	count_time_cpp(47)

if __name__ == '__main__':
	main()


"""What is the result for Fibonacci with n=47? Why?"""
#fib_cpp takes 3.5762786865234375e-06 seconds to run