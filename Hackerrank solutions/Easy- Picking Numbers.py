"""
Picking Numbers: https://www.hackerrank.com/challenges/picking-numbers/problem

"""

#!/bin/python3

import math
import os
import random
import re
import sys

def pickingNumbers(n,a):
    a.sort()
    m=max(a)
    res=[0]*m
    for i in range(n):
        k=a[i]
        res[k]+=1
    for i in range(n-1):
        k=a[i]
        l=a[i+1]
        s=res(k)+res(l)
        print(s)

    
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(n,a)

    fptr.write(str(result) + '\n')

    fptr.close()
