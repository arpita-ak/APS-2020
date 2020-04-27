"""
COVIDLQ

"""

for z in range(int(input())):
    N=int(input())
    P=list(map(int,input().strip().split()))
    flag=0
    for i in range(N):
        if P[i]==1:
            for j in range(i+1,N):
                if P[j]==1:
                    if j-i<6:
                        flag=1
                        break
                
    if flag==0:
        print("YES")
    if flag==1:
        print("NO")