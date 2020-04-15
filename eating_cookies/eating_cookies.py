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
        return 0
    # If less than 0, return 0.

    # To get all of the possible values
    # We can subtract 1, 2, or 3,
    #     and then call this funciton again.
    # Once we hit zero,
    #     we return 1 and boomerang back up the stack.
    return eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3)


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
            ways=eating_cookies(num_cookies), n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')
