"""
Minimum Distances: https://www.hackerrank.com/challenges/minimum-distances/problem

"""

import math
import os
import random
import re
import sys

def minimumDistances(n,a):
    m=n
    for x in range(n):
        d=(n -1 - a[::-1].index(x))-a.index(x)
        if d<m:
            m=d
    return m



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(n,a)

    fptr.write(str(result) + '\n')

    fptr.close()
