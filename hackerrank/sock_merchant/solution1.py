#!/bin/python3

import collections
import os


def sockMerchant(n, ar):
    counts = collections.defaultdict(int)
    for color in ar:
        counts[color] += 1

    ans = 0
    for _, count in counts.items():
        ans += count // 2

    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
