"""
HackerRank in a String!: https://www.hackerrank.com/challenges/hackerrank-in-a-string/problem

"""

import math
import os
import random
import re
import sys

# Complete the hackerrankInString function below.
def hackerrankInString(s):
    t="hackerrank"
    le=len(t)
    j=0
    l=len(s)
    for i in range(l):
        if s[i]==t[j]:
            j+=1
        if j==le:
            return "YES"
        
    return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)

        fptr.write(result + '\n')

    fptr.close()
