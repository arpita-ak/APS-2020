"""
Hackerrank Diagonal Difference: https://www.hackerrank.com/challenges/diagonal-difference/problem
    
"""

import os

def diagonalDifference(n,arr):
    ps=0
    ss=0
    for i in range(n):
        for j in range(n):
            if i==j:
                ps=ps+arr[i][j]
            if i+j==n-1:
                ss=ss+arr[i][j]

    return abs(ps-ss)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(n,arr)

    fptr.write(str(result) + '\n')

    fptr.close()
