
"""
Jumping on the Clouds:https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem

"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(n,c):
    i=0
    k=0
    while i<n-2:
        if c[i+2]==0:
            i+=2
            k+=1
            print(i,k,c[i],n-i)
        elif c[i+2]==1 and c[i+1]==0:
            i+=1
            k+=1
            print(i,k,c[i],n-i)    
       

    return k




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(n,c)

    fptr.write(str(result) + '\n')

    fptr.close()
