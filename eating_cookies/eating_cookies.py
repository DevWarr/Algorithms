#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution


def eating_cookies(n, cache=None):

    if n == 0:
        # If zero, return 1.
        return 1

    if n < 0:
        # If less than 0, return 0.
        return 0

    if cache is None:
        # No cache → create one
        cache = [0] * (n+1)

    # To get all of the possible values
    # We can subtract 1, 2, or 3,
    #     and then call this funciton again.
    # Once we hit zero,
    #     we return 1 and boomerang back up the stack.
    # BUT, instead of creating a thousand recursive calls,
    # Let's store our values in a cache as we go.

    # Check our cache for the values minus 1, 2, and 3
    minus_3 = cache[n-3]
    minus_2 = cache[n-2]
    minus_1 = cache[n-1]
    # ==============================================
    #  NOTE:
    # If we get values -1 or -2 (2-3 or 1-3), 
    #     our cache will still return 0.
    # That's because we don't know (yet) what n or n-1 are
    # Until the function's almost done boomeranging back up the stack.
    # ==============================================

    # If our cache doesn't have the proper value (It should never be zero)
    if minus_3 == 0:
        minus_3 = cache[n-3] = eating_cookies(n-3, cache)
    if minus_2 == 0:
        minus_2 = cache[n-2] = eating_cookies(n-2, cache)
    if minus_1 == 0:
        minus_1 = cache[n-1] = eating_cookies(n-1, cache)

    return minus_1 + minus_2 + minus_3


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
            ways=eating_cookies(num_cookies), n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')
