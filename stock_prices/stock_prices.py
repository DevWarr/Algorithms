#!/usr/bin/python

import argparse


def find_max_profit(prices):
    if len(prices) < 2:
        return 0

    # Create a minimum price and a maximum profit
    # min_price is our starting point,
    #     'cause we have to start somewhere.
    # max_profit is 2nd - 1st values,
    #     'cause, again, we have to start somewhere.
    min_price = prices[0]
    max_profit = prices[1] - prices[0]
    for i in range(len(prices)):

        if prices[i] < min_price:
            # If our value is less than our min_price
            # look for a max profit contender
            for j in range(i+1, len(prices)):
                if prices[j] - prices[i] > max_profit:
                    # If we find two numbers that gives us a higher profit,
                    # Update our smallest number and max_profit
                    min_price = prices[i]
                    max_profit = prices[j] - prices[i]

    # And return max_profit when done
    return max_profit


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
