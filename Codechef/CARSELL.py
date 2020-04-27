"""
CARSELL

"""

for z in range(int(input())):
    N=int(input())
    P=list(map(int,input().strip().split()))
    
    P.sort(reverse=1)
    s=0
    for i in range(N):
        if P[i]-i>0:
            s+=P[i]-i
    print(s%(pow(10,9)+7))
    