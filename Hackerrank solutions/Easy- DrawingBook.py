"""
Drawing Book: https://www.hackerrank.com/challenges/drawing-book/problem

"""

#!/bin/python3

import os
import sys

#
# Complete the pageCount function below.
#
def pageCount(n, p):
    front=0
    back=0
    if n%2==0:
        if p%2==0:
            front=p/2
            back=(n-p)/2
        else:
            front=(p-1)/2
            back=(n-p+1)/2
    else:
        if p%2==0:
            front=p/2
            back=(n-p)/2
        else:
            front=(p-1)/2
            back=(n-p)/2

    return int(min(front,back))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    p = int(input())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()
