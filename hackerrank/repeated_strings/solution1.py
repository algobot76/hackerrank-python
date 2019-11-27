#!/bin/python3

import itertools
import os

# TLE
def repeatedString(s, n):
    sc = itertools.cycle(s)
    ans = 0
    while n > 0:
        ch = next(sc)
        if ch == 'a':
            ans += 1
        n -= 1
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
