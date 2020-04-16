#!/usr/bin/python

import sys
import time

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution

def O_time(n):
    a = time.time()
    res = eating_cookies(n)
    b = time.time()
    print(b-a)
    return res


def eating_cookies(n, cache=None):
    # Create our base array with our base cases
    # 1 way  to eat 0 cookies
    # 1 way  to eat 1 cookie
    # 2 ways to eat 2 cookies
    cache = [1,1,2] + [0] * (n-2)
    
    for i in range(3, n+1):
        # n IS a number we want to reach,
        # so we want to stop at
        #     n+1 instead of just n
        cache[i] = cache[i-1] + cache[i-2] + cache[i-3]
    return cache[n]



if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
            ways=eating_cookies(num_cookies), n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')
