"""
Beautiful Triplets:https://www.hackerrank.com/challenges/beautiful-triplets/problem

"""
import math
import os
import random
import re
import sys


def beautifulTriplets(d, arr):
    sarr = set(arr)
    return len([c for c in arr if c + d in sarr and c + 2 * d in sarr])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    arr = list(map(int, input().rstrip().split()))

    result = beautifulTriplets(d, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
