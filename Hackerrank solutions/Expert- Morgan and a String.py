"""
Morgan and a String: https://www.hackerrank.com/challenges/morgan-and-a-string/problem

"""
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the morganAndString function below.
def morganAndString(a, b):
    la=len(a)
    lb=len(b)
    a=a+'z'
    b=b+'z'
    
    topa=0
    topb=0
    ans=''
    flaga=0
    flagb=0
    for i in range(la+lb):
        m=''
        
        if topa>=la:
            m=b[topb:]
            flagb=1
            if flagb==1:
                ans=ans+m+a[topa:]
                #print(ans)
                break

        elif topb>=lb:
            m=a[topa:]
            flaga=1
            if flaga==1:
                ans=ans+m+b[topb:]
                #print(ans)
                break
            
        elif a[topa]==b[topb]:
            k=min(a[topa:],b[topb:])
            m=k[0]
            if k==a[topa:]:
                topa+=1
            elif k==b[topb:]:
                topb+=1
        else:
            m=min(a[topa],b[topb])
            if m==a[topa]:
                topa+=1
            elif m==b[topb]:
                topb+=1
        #print(m)
        ans=ans+m
    l=len(ans)
    return ans[:l-2]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        a = input()

        b = input()

        result = morganAndString(a, b)

        fptr.write(result + '\n')

    fptr.close()

