"""
String Similarity: https://www.hackerrank.com/challenges/string-similarity/problem

"""

#!/bin/python3

import math
import os
import random
import re
import sys

def stringSimilarity(string):
    n = len(string)
    z=[0]*n
    l, r, k = 0, 0, 0
    for i in range(1, n): 
        if i > r: 
            l, r = i, i 
            while r < n and string[r - l] == string[r]: 
                r += 1
            z[i] = r - l 
            r -= 1
        else: 
            k = i - l 
            if z[k] < r - i + 1: 
                z[i] = z[k] 
            else: 
                l = i 
                while r < n and string[r - l] == string[r]: 
                    r += 1
                z[i] = r - l 
                r -= 1
    return n+sum(z)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = stringSimilarity(s)

        fptr.write(str(result) + '\n')

    fptr.close()
