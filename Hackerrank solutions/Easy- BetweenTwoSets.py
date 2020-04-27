"""
Between Two Sets: https://www.hackerrank.com/challenges/between-two-sets/problem

"""

import os

def getTotalX(n, m, a, b):
    c=0
    c1=0
    c2=0
    for i in range(a[n-1],b[0]+1):
        for j in range(n):
            if i%a[j]==0:
                c1=c1+1
        for k in range(m):
            if b[k]%i==0:
                c2=c2+1
        if c1==n and c2==m:
            c=c+1  
        c1=0
        c2=0    
    return c


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(n,m,arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
