"""
SNUGFIT

"""

T=int(input())

for i in range(T):
    N=int(input())
    A=list(map(int,input().strip().split()))
    B=list(map(int,input().strip().split()))
    
    A.sort()
    B.sort()
    s=0
    
    for i in range(N):
        s+=min(A[i],B[i])
        
    print(s)