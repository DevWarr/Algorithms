#!/usr/bin/python

import sys

def update_cache(cache, val, current_denomination):
    for i in cache:
        if i > current_denomination:
            cache[i] += val

def making_change(amount, denominations, current_den=None, cache=None):

    if amount == 0 or amount == 1 or amount == 2 or amount == 3 or amount == 4:
        # Only one way to make these numbers!
        return 1

    # Initialize i and cache
    if cache is None:
        cache = {}
    i = current_den if current_den is not None else len(denominations) - 1

    # Check to see if our cache has the answer:
    # 
    #   amount
    #   ↓
    #   ↓    denominations
    # { ↓    ↓      ↓
    #   5:  {5: 2, 10: 2},
    #   10: {5: 3, 10: 4},
    #   20: {5: 5, 10: 9}
    # }
    check = cache.get(amount, None)
    if check is None:
        # If we don't have a dict for our current amount, create one
        check = cache[amount] = {}

    different_ways = 0

    while i >= 0:
        # We're going to keep looping,
        # starting at the highest denomination and moving down

        # Do we have a count for this specific denomination value?
        # If we do, add it to our different ways, and break
        cached_ways = check.get(denominations[i], None)
        if cached_ways is not None:
            different_ways += cached_ways
            break

        if amount - denominations[i] < 0:
            # If our amount minus the current denomination is negative,
            # The coin value is too big!
            # Move down to the next smaller coin, and reset the loop.
            i -= 1
            continue

        if denominations[i] == 1:
            # If our current value is the penny, 
            # there's only one way left to make change:
            # 100% pennies
            # Update the cache[amount] dict,
            #     update different_ways, 
            #     and break
            update_cache(check, 1, denominations[i])
            different_ways += 1
            break

        # recurse, continuing to make change.
        # WHEN RECURSING, make sure to include our current denomination.
        # This will make sure we don't double up on coin combos.
        # Example:
        #    15 cents - 1 dime   ->  5 cents - 1 nickel = 1 dime, 1 nickel
        #    15 cents - 1 nickel -> 10 cents - 1 dime   = 1 dime, 1 nickel
        #     ↑↑ BAD, because once we subtract a nickel, we should
        #             only allow coin values of a nickel or smaller
        #
        coin_ways = making_change(amount - denominations[i], denominations, i, cache)
        update_cache(check, coin_ways, denominations[i])
        check[denominations[i]] = coin_ways
        different_ways += coin_ways
        i -= 1
    return different_ways


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python making_change.py [amount]` with different amounts
    if len(sys.argv) > 1:
        denominations = [1, 5, 10, 25, 50]
        amount = int(sys.argv[1])
        print("There are {ways} ways to make {amount} cents.".format(
            ways=making_change(amount, denominations), amount=amount))
    else:
        print("Usage: making_change.py [amount]")
