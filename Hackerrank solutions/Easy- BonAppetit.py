"""
Bon Appetit: https://www.hackerrank.com/challenges/bon-appetit/problem

"""

def bonAppetit(n, k, b, ar):
    annaBill = sum(ar[i] for i in range(n) if i != k)//2
    return 'Bon Appetit' if annaBill == b else str(b-annaBill)

if __name__ == '__main__' :
    
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    km=bonAppetit(n, k, b, bill)
    print(km)
