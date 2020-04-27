"""
Cats and a Mouse: https://www.hackerrank.com/challenges/cats-and-a-mouse/problem

"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the catAndMouse function below.
def catAndMouse(x, y, z):
    catA=abs(x-z)
    catB=abs(y-z)
    if catA==catB:
        return 'Mouse C'
    if catA>catB:
        return 'Cat B'
    if catB>catA:
        return 'Cat A'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)

        fptr.write(result + '\n')

    fptr.close()
