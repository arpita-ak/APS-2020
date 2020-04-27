"""

Sock Merchant: https://www.hackerrank.com/challenges/sock-merchant/problem
"""

import os

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    m=max(ar)
    sock=[0]*(m+1)
    k=0
    for i in range(n):
        k=ar[i]
        sock[k]+=1
    
    s=0
    for i in range(m+1):
        s+= sock[i]//2
    
    return s

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
