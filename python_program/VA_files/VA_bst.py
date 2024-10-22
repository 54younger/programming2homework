"""
Solutions to module VA bst

Student: Chenyang Wang
Mail: chenyang.wang.6882@student.uu.se
"""
import random

class BST:

    class Node:
        def __init__(self, key, left=None, right=None):
            self.key = key
            self.left = left
            self.right = right

        def __iter__(self):     # Discussed in the text on generators
            if self.left:
                yield from self.left
            yield self.key
            if self.right:
                yield from self.right

    def __init__(self, root=None):
        self.root = root

    def __iter__(self):         # Discussed in the text on generators
        if self.root:
            yield from self.root

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, r, key):
        if r is None:
            return self.Node(key)
        elif key < r.key:
            r.left = self._insert(r.left, key)
        elif key > r.key:
            r.right = self._insert(r.right, key)
        else:
            pass  # Already there
        return r

    def print(self):
        self._print(self.root)

    def _print(self, r):
        if r:
            self._print(r.left)
            print(r.key, end=' ')
            self._print(r.right)

    def contains(self, k):
        n = self.root
        while n and n.key != k:
            if k < n.key:
                n = n.left
            else:
                n = n.right
        return n is not None

    def size(self):
        return self._size(self.root)

    def _size(self, r):
        if r is None:
            return 0
        else:
            return 1 + self._size(r.left) + self._size(r.right)



    def ipl(self):   
        if self.root is None:
            return 0
        return self._ipl(self.root, 1)
    def _ipl(self, r, depth):
        if r is None:
            return 0
        return depth + self._ipl(r.left, depth+1) + self._ipl(r.right, depth+1)

    def height(self):                 #
        if self.root is None:
            return 0
        else:
            return self._height(self.root)

    def _height(self, r):
        if r is None:
            return 0
        else:
            return 1 + max(self._height(r.left), self._height(r.right))


def random_tree(n):
    t = BST()
    for _ in range(n):
        t.insert(random.random())
    return t

def permutations(n):
    import math
    return 1.39 * math.log(n, 2)

        
def main():
    t = BST()
    ob_height = []
    IPL_d_n = []
    exp_height = []
    for k in range(1, 9):
        n = 1000 * 2 ** k
        t = random_tree(n)
        ob_height.append(t.height())
        IPL_d_n.append(t.ipl()/n)
        exp_height.append(permutations(n))
        print(f"observed height ={ob_height[k-1]} \n IPL/n = {IPL_d_n[k-1]}")
        print(f"expected height = {exp_height[k-1]}\n")
    #draw the plot
    import matplotlib.pyplot as plt
    plt.plot(ob_height, label='observed height')
    plt.plot(IPL_d_n, label='IPL/n')
    plt.plot(exp_height, label='expected height')
    plt.legend()
    plt.show()

        

if __name__ == "__main__":
    main()


"""

Results for ipl of random trees
===============================
How well does that agree with the theory?
It's pretty close to the expected height. 

What can you guess about the height?
The observed height is higher than the expected height.

"""
