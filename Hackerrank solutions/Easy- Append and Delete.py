"""
Append and Delete: https://www.hackerrank.com/challenges/append-and-delete/problem

"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the appendAndDelete function below.
def appendAndDelete(s, t, k):
    if s==t:
        return('Yes')
    n=len(s)
    m=len(t)
    if m>n:
        return('No')
    c=0
    for i in range(min(m,n)):
        if s[i]==t[i]:
            c+=1
        else:
            break
    
    if k>= (m-c)+(n-c):
        return('Yes')
    else:
        return('No')



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
