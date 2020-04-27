"""
Birthday Cake Candles:https: //www.hackerrank.com/challenges/birthday-cake-candles/problem
    
"""

import os

# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(n,ar):
    a=0
    m=max(ar)
    for i in range(n):
        if ar[i]==m:
            a+=1
    return a

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n= int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(n,ar)

    fptr.write(str(result) + '\n')

    fptr.close()
