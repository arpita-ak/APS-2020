"""
STRNO

"""

import math as mt 

T=int(input()) 

for i in range(T):
    n,k=map(int,input().strip().split())
    a = 0
    while n%2==0:
        a+=1
        n = n // 2
    for i in range(3, mt.ceil(mt.sqrt(n)), 2):
        while n % i == 0:
            n = n / i;
            a+=1
    if n>2:
        a+=1
    if a < k:
        print(0)
    else:
        print(1)