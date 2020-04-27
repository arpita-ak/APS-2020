"""
CHPINTU

"""

T=int(input())

for i in range(T):
    n=list(map(int,input().strip().split()))
    N=n[0]
    M=n[1]
    F=list(map(int,input().strip().split()))
    C=list(map(int,input().strip().split()))
    
    freq = {} 
    for i in range(N):
        k=F[i]
        if k in freq: 
            freq[k] = freq[k]+C[i]
        else: 
            freq[k] = C[i]
    
    m=min(freq.values())
    print(m)
            