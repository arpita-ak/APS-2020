"""
Climbing the Leaderboard: https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem

"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the climbingLeaderboard function below.
def climbingLeaderboard(s, scores, a, alice):
    uniq=[0]*(s+a)
    j=0
    for i in scores:
        if i not in uniq:
            uniq[j]=i
            j+=1
    print(uniq)

    for i in range(a):
        for k in range(j):
            if uniq[k]<alice[i]<uniq[k+1]:
                
                uniq[k+1]=alice[i]
                


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = int(input())

    scores = list(map(int, input().rstrip().split()))

    a = int(input())

    alice = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(s, scores, a, alice)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
