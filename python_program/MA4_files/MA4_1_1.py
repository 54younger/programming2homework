
"""
Solutions to module 4
Review date:
"""

student = ""
reviewer = ""


import random as r
import matplotlib.pyplot as plt
import math

def approximate_pi(n):
    inside_circle = 0
    x_inside = []
    y_inside = []
    x_outside = []
    y_outside = []
    print(f"Builtin constant π: {math.pi}")
    for _ in range(n):
        x = r.uniform(-1, 1)
        y = r.uniform(-1, 1)
        if x**2 + y**2 <= 1:
            inside_circle += 1
            x_inside.append(x)
            y_inside.append(y)
        else:
            x_outside.append(x)
            y_outside.append(y)

    pi_approx = 4 * inside_circle / n

    print(f"Number of points inside the circle: {inside_circle}")
    print(f"Approximation of π: {pi_approx}")

    plt.figure(figsize=(6, 6))
    plt.scatter(x_inside, y_inside, color='red', s=1)
    plt.scatter(x_outside, y_outside, color='blue', s=1)
    plt.gca().set_aspect('equal', adjustable='box')
    plt.savefig(f"pi_{n}.png")
    #plt.show()
    return pi_approx

def main():
    dots = [1000, 10000, 100000]
    for n in dots:
        approximate_pi(n)

if __name__ == '__main__':
    main()
