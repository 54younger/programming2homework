# https://docs.python.org/3/library/unittest.html
import unittest

from MA1 import *


class Test(unittest.TestCase):

    def test_count(self):
        ''' Reasonable tests
        1. search empty lists
        2. count first, last and interior elements
        3. search for a list
        4. check that sublists on several levels are searched
        5. search non existing elements
        6. check that the list searched is not destroyed
        '''
        
        print('\nTests count')

        test1 = []
        #test2 = [1,2,3,1]
        test_rest = [[1,2],3,[2,1,'a',[1,2]],[1,2]]
        test_6 = test_rest

        self.assertEqual(count(1,test1),0)      #1
        self.assertEqual(count(1,test_rest),4)  #2
        self.assertEqual(count([1,2],test_rest),3)  #3 4
        self.assertEqual(count('1',test_rest),0) #5
        self.assertEqual(test_rest, test_6)     #6

        print('*** Should be implemented!***')


if __name__ == "__main__":
    unittest.main()
