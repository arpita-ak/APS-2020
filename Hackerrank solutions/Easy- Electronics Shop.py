"""
Electronics Shop: https://www.hackerrank.com/challenges/electronics-shop/problem

"""

import os

def getMoneySpent(k, d, b,n,m):
    if k[0]+d[0]>=b:
        return -1
    else:
        cost=k[n-1]+d[m-1]
        if cost<b:
            return cost
        while cost>b and n>=0 and m>=0:
            cost=k[n-1]+d[m-1]
            n=n-1
            m=m-1
        return cost

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    moneySpent = getMoneySpent(keyboards, drives, b, n, m)

    fptr.write(str(moneySpent) + '\n')

    fptr.close()
