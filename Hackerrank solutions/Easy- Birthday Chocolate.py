"""
Birthday Chocolate: https://www.hackerrank.com/challenges/the-birthday-bar/problem

"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthday function below.
def birthday(n, s, d, m):
    sumn=0
    for j in range(m):
            sumn=sumn+s[j]
    if sumn==d:
        c=1
    else:
        c=0

    for i in range(n-m):
        sumn=sumn-s[i]+s[i+m]
        if sumn==d:
            c=c+1
    return c

        


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(n, s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
