""" linked_list.py

Student:Chenyang Wang
Mail:chenyang.wang.6882@student.uu.se
Reviewed by: Behnam
Date reviewed:2024/10/8
"""


class LinkedList:

    class Node:
        def __init__(self, data, succ):
            self.data = data
            self.succ = succ

    def __init__(self):
        self.first = None

    def __iter__(self):            # Discussed in the section on iterators and generators
        current = self.first
        while current:
            yield current.data
            current = current.succ

    def __in__(self, x):           # Discussed in the section on operator overloading
        for d in self:
            if d == x:
                return True
            elif x < d:
                return False
        return False

    def insert(self, x):
        if self.first is None or x <= self.first.data:
            self.first = self.Node(x, self.first)
        else:
            f = self.first
            while f.succ and x > f.succ.data:
                f = f.succ
            f.succ = self.Node(x, f.succ)

    def print(self):
        print('(', end='')
        f = self.first
        while f:
            print(f.data, end='')
            f = f.succ
            if f:
                print(', ', end='')
        print(')')

    # To be implemented

    def length(self):
        if self.first is None:
            return 0
        count = 1
        f = self.first
        while f.succ:
            f = f.succ
            count += 1
        return count

    def mean(self):
        pass

    def remove_last(self):       #
        if self.first is None:
            raise ValueError('List is empty')
        f = self.first
        if f.succ is None:
                result = f.data
                self.first = None
                return result
        while f.succ.succ:
            f = f.succ
        result = f.succ.data
        f.succ = None
        return result


    def remove(self, x):
        f = self.first
        if f.data == x:
            self.first = f.succ
            return True

        while f.succ:
            if f.succ.data < x:
                f = f.succ
            elif f.succ.data == x:
                f.succ = f.succ.succ
                return True
            else:
                break

        return False



    def to_list(self):            #
        list = []
        for x in self:
            list.append(x)
        return list

    def remove_all(self, x):      #
        count = 0
        while self.first.data == x:
            self.first = self.first.succ
            count += 1
            if self.first is None:
                return count

        f = self.first
        while f.succ:
            if f.succ.data == x:
                f.succ = f.succ.succ
                count += 1
            else:
                f = f.succ

    def __str__(self):
        if self.first is None:
            return '()'
        string = '('
        for x in self:
            string += str(x) + ', '

        string = string[:-2] + ')'
        return string

    def copy(self):               #

        result = LinkedList()
        for x in self:
            result.insert(x)
        return result
        '''
        Complexity for this implementation: O(n^2)
        '''


    def copy(self):               # Should be more efficient

        new_list = LinkedList()
        if self.first is None:
            return new_list
        f = self.first
        new_list.first = self.Node(f.data, None)
        new_f = new_list.first
        while f.succ:
            new_f.succ = self.Node(f.succ.data, None)
            f = f.succ
            new_f = new_f.succ

        return new_list

    ''' Complexity for this implementation: O(n)

    '''

def main():
    lst = LinkedList()
    for x in [1, 1, 1, 2, 3, 3, 2, 1, 9, 7]:
        lst.insert(x)
    lst.print()

    # Test code:


if __name__ == '__main__':
    main()
