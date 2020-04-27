"""
Beautiful Days at the Movies: https://www.hackerrank.com/challenges/beautiful-days-at-the-movies/problem

"""

#!/bin/python3

import math
import os
import random
import re
import sys

def reverse(n):
    s=str(n)
    t=s[::-1]
    t=int(t)
    return t

# Complete the beautifulDays function below.
def beautifulDays(i, j, k):
    rev=0
    c=0
    diff=0
    for num in range(i,j+1):
        rev=reverse(num)
        diff=abs(rev-num)
        if diff%k ==0:
            c+=1
    return c
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ijk = input().split()

    i = int(ijk[0])

    j = int(ijk[1])

    k = int(ijk[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()
