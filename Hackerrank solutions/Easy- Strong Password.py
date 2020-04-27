"""
Strong Password:https://www.hackerrank.com/challenges/strong-password/problem

"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumNumber function below.
def minimumNumber(n, p):
    c=0
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special = "!@#$%^&*()-+"
    a=[0,0,0,0]
    for i in range(n):
        if p[i] in numbers:
            a[0]=1
        if p[i] in lower_case:
            a[1]=1
        if p[i] in upper_case:
            a[2]=1
        if p[i] in special:
            a[3]=1
    
    for i in range(4):
        if a[i]==0:
            c+=1
    
    return max(c,6-n)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
