#!/bin/python3

import os


def countingValleys(n, s):
    sea = 0
    ans = 0
    for ch in s:
        if ch == 'D':
            sea -= 1
        else:
            sea += 1
        if ch == 'U' and sea == 0:
            ans += 1
    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
