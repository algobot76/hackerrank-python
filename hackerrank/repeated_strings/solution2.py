#!/bin/python3

import collections
import os


def repeatedString(s, n):
    count = collections.Counter(s[:n])['a']
    if n <= len(s):
        return count

    ans = count * (n // len(s))
    for i in range(n % len(s)):
        if s[i] == 'a':
            ans += 1

    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
