#!/usr/bin/python

import sys


def rock_paper_scissors(n):

    if n < 1:
        return [[]]

    if n == 1:
        return [["rock"], ["paper"], ["scissors"]]

    # Add our arrays together recursively
    R = [["rock"] + rps for rps in rock_paper_scissors(n-1)]
    P = [["paper"] + rps for rps in rock_paper_scissors(n-1)]
    S = [["scissors"] + rps for rps in rock_paper_scissors(n-1)]

    return R + P + S


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
