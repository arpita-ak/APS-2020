"""
Migratory Birds: https://www.hackerrank.com/challenges/migratory-birds/problem

"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    l=len(arr)
    m=max(arr)
    array=[0]*(m+1)
    k=0

    print(len(array))

    for i in range(l):
        k=arr[i]
        array[k]+=1

    maximum=max(array)
    mini=0

    for i in range(m+1):
        if array[i]==maximum:
            mini=i
            break
    return mini
       

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
