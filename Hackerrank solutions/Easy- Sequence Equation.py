"""
Sequence Equation:https://www.hackerrank.com/challenges/permutation-equation/problem

"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the permutationEquation function below.
def permutationEquation(p):
    l=len(p)
    return (p.index(p.index(i)+1)+1 for i in range(1,l+1))




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
