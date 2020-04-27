"""
SALARY

"""

t=int(input())

for i in range(t):
    n=list(map(int,input().strip().split()))
    sal=list(map(int,input().strip().split()))
    m=min(sal)
    l=len(sal)
    dif=0
    for i in range(l):
        dif+=(sal[i]-m)
    print(dif)