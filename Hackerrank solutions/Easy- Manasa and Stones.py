"""
Manasa and Stones:https://www.hackerrank.com/challenges/manasa-and-stones/problem

"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the stones function below.

if __name__ == '__main__':
    
    T = int(input())

    for T_itr in range(T):
        n = int(input())

        a = int(input())

        b = int(input())
        print(' '.join(map(str,sorted({x*a+(n-1-x)*b for x in range(n)}))))
    
