"""
CamelCase: https://www.hackerrank.com/challenges/camelcase/problem

"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the camelcase function below.
def camelcase(s):
    c=1
    for i in range(len(s)):
        if 'A'<=s[i]<='Z':
            c+=1
    return c

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = camelcase(s)

    fptr.write(str(result) + '\n')

    fptr.close()
