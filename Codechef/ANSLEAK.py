"""
ANSLEAK 

"""

import random

T=int(input())

for i in range(T):
    N,M,K=list(map(int,input().strip().split()))
    for z in range(N):
        cij=list(map(int,input().strip().split()))
        r=random.randint(1,M)
        flag=0
        while(flag==0):
            if r in cij:
                print(r,end=' ')
                flag=1
            else:
                r=random.randint(1,M)
        
    

   
    