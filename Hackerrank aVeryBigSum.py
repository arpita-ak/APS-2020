"""
Hackerrank aVeryBigSum: https://www.hackerrank.com/challenges/a-very-big-sum/problem
    
"""

import os

def aVeryBigSum(ar):
    s=0
    for i in range(len(ar)):
        s=s+ar[i]
    return s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
