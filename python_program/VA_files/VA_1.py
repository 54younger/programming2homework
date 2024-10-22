"""
Solutions to module VA 1
Student: Chenyang Wang
Mail: chenyang.wang.6882@student.uu.se
"""
import sys
import time
sys.setrecursionlimit(1000000)
def exchange(a, coins):
    num_coins = [[-1] * (a+1) for _ in range(len(coins)+1)]

    def _exchange(a, coins):  
        b = len(coins)
        if a == 0:
            return 1
        if a < 0 or not coins or a < coins[0] or a%coins[0] != 0:
            return 0
        if num_coins[b][a] == -1:
            num_coins[b][a] = _exchange(a-coins[0], coins) + _exchange(a, coins[1:])
        return num_coins[b][a]
    return _exchange(a, coins)
    '''
def exchange(a, coins):
    if a == 0:
        return 1
    if a < 0 or not coins or a < coins[0] or a%coins[0] != 0:
        return 0
    return exchange(a-coins[0], coins) + exchange(a, coins[1:])
'''
def zippa(l1: list, l2: list) -> list: 
    """ Returns a new list from the elements in l1 and l2 like the zip function"""
    new_list = []
    for x in range(min(len(l1), len(l2))):
        new_list.append(l1[x])
        new_list.append(l2[x])
    for x in range(min(len(l1), len(l2)), max(len(l1), len(l2))):
        if len(l1) > len(l2):
            new_list.append((l1[x]))
        else:
            new_list.append((l2[x]))
    return new_list


def count_time(func, *args):
    time1 = time.time()
    func(*args)
    time2 = time.time()
    return time2 - time1


def main():
    coins = [1, 5, 10, 50, 100]
    print('\nCode that demonstates my implementations\n')
    print(count_time(exchange,10000, coins))
    print(count_time(exchange,2000, coins))
    print(count_time(exchange,1000, coins))


if __name__ == "__main__":
    main()

####################################################

"""
  Answers to the none-coding tasks
  ================================
  
  
  Exercise 1

What time did it take to calculate large sums such as 1000 and 2000? 

What happens if you try to calculate e.g. 10000?
time of 10000:  0.004098653793334961    s
time of 2000:   0.0007145404815673828   s
time of 1000:   0.0003447532653808594   s
  
"""
