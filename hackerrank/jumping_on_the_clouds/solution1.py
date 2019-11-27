#!/bin/python3

import os
import sys


def jumpingOnClouds(c):
    n = len(c)
    dp = [0] * n
    for i in range(n):
        if c[i] == 1:
            dp[i] = sys.maxsize
    dp[1] = 1
    for i in range(2, n):
        if dp[i] == sys.maxsize:
            continue
        dp[i] = min(dp[i - 1], dp[i - 2]) + 1

    return dp[n - 1]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
