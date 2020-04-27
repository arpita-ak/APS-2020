"""
CASH

"""

T=int(input())

for i in range(T):
    n=list(map(int, input().strip().split()))
    N=n[0]
    K=n[1]
    a=list(map(int, input().strip().split()))
    s=sum(a)
    print(s%K)