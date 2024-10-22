""" bst.py

Student:Chenyang Wang
Mail:chenyang.wang.6882@student.uu.se
Reviewed by: Behnam
Date reviewed:2024/10/8
"""


from linked_list import LinkedList


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

    def __iter__(self):         # Dicussed in the text on generators
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

    def contains(self, k): #
        return self._contains(self.root, k)

    def _contains(self, r, k):
        if r is None:
            return False
        elif k < r.key:
            return self._contains(r.left, k)
        elif k > r.key:
            return self._contains(r.right, k)
        else:
            return True



    def size(self):
        return self._size(self.root)

    def _size(self, r):
        if r is None:
            return 0
        else:
            return 1 + self._size(r.left) + self._size(r.right)

#
#   Methods to be completed
#

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

    def remove(self, key): #
        self.root = self._remove(self.root, key)

    def _remove(self, r, k):                      #
        if r is None:
            return None
        elif k < r.key:
            # r.left = left subtree with k removed
            r.left = self._remove(r.left, k)
        elif k > r.key:
            # r.right =  right subtree with k removed
            r.right = self._remove(r.right, k)

        else:  # This is the key to be removed
            if r.left is None:     # Easy case
                return r.right
            elif r.right is None:  # Also easy case
                return r.left
            else:
                # This is the tricky case.
                # Find the smallest key in the right subtree
                # Put that key in this node
                # Remove that key from the right subtree
                temp = r.right
                while temp.left:
                    temp = temp.left
                r.key = temp.key
                r.right = self._remove(r.right, temp.key)
        return r

    def __str__(self):                #
        result = '<'
        if self.root is None:
            return result + '>'
        else:
            for x in self:
                result += str(x) + ', '
            return result[:-2] + '>'



    def to_list(self):                      #
        list = []
        for x in self:
            list.append(x)
        return list
    # Complexity: O(n)

    def to_LinkedList2(self):                 #
        result = LinkedList()
        for x in self:
            result.insert(x)
        return result
    # Complexity: O(n^2)
    def to_LinkedList(self):
        def _to_LinkedList(root, lst):
            if root.right != None:
              _to_LinkedList(root.right, lst)
            lst.insert(root.key)
            if root.left != None:
              _to_LinkedList(root.left, lst)
                             #
        result = LinkedList()
        _to_LinkedList(self.root, result)
        return result

def random_tree(n):                               # Useful
    pass


def main():
    t = BST()
    for x in [4, 1, 3, 6, 7, 1, 1, 5, 8]:
        t.insert(x)
    t.print()
    print()

    print('size  : ', t.size())
    for k in [0, 1, 2, 5, 9]:
        print(f"contains({k}): {t.contains(k)}")


if __name__ == "__main__":
    main()


"""
What is the generator good for?
==============================

1. computing size? yes, sum(1 for x in t)
2. computing height? no, need to recurse the subtrees height
3. contains? yse, any(k == x for x in t)
4. insert? no, need to recurse the subtrees
5. remove? no, need to adjust the tree

"""
