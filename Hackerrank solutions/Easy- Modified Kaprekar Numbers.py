"""
Modified Kaprekar Numbers:https://www.hackerrank.com/challenges/kaprekar-numbers/problem

"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the kaprekarNumbers function below.
def kaprekarNumbers(p, q):
    flag=0
    if p==1 and q>10:
        print('1 9',end=' ')
        p=p+10
        flag=1

    for i in range(p+1,q+1):
        d1=math.floor(math.log(i, 10)+1)
        s=i*i
        d2=math.floor(math.log(s, 10)+1)
        s=str(s)
        r=s[d2-d1:]
        l=s[:d2-d1]
        #print(i,s,r,l)
        if int(r)+int(l)==i:
            print(i,end=' ')
            flag=1
    if flag==0:
            print("INVALID RANGE")


if __name__ == '__main__':
    p = int(input())

    q = int(input())

    kaprekarNumbers(p, q)
