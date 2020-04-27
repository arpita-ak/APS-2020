"""
Repeated String: https://www.hackerrank.com/challenges/repeated-string/problem

"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    l=len(s)
    c=0
    for i in range(l):
        if s[i]=='a':
            c+=1
    q = n//l
    r = n%l
    n = n-q*l
    c = c*q
    for i in range(n):
        if s[i]=='a':
            c+=1
    return c

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
