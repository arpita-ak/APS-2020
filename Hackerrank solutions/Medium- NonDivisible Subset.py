"""
Non-Divisible Subset:https://www.hackerrank.com/challenges/non-divisible-subset/problem

"""
#!/bin/python3

import math
import os
import random
import re
import sys



n, k = map(int,input().strip().split(" "))

arr = list(map(int,input().strip().split(" ")))

d = {x:[] for x in range(k)}

for i in range(n): 
    t=arr[i]%k
    d[t].append(arr[i])

count = 0

if len(d[0]) > 0:
    count = 1
S = set([(x,k-x) for x in range(1,k//2+1)])

for i,j in S:
    if i != j:
        if len(d[i]) > len(d[j]):
            count += len(d[i])
        else:
            count += len(d[j])
    else:
        if len(d[i]) > 0:
            count += 1
print(count)
