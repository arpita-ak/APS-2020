"""
Pangrams: https://www.hackerrank.com/challenges/pangrams/problem

"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the pangrams function below.
def pangrams(s):
    l=len(s)
    arr=[0]*26
    for i in range(l):
        k=ord(s[i])
        if 97<=k<=122:
            arr[k-97]=1
        elif 65<=k<=90:
            arr[k-65]=1
    for i in range(26):
        if arr[i]==0:
            return "not pangram"
    return "pangram"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
