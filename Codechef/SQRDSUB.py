"""
SQRDSUB

"""
T=int(input())

def zeroes(i):
    t=i-1
    l=0
    flag=0
    while (t>=0) and flag==0:
        if b[t]==0:
            l+=1
            t-=1
        else:
            flag=1
    
    t=i+1
    r=0
    flag=0
    while (t<N) and flag==0:
        if b[t]==0:
            r+=1
            t+=1
        else:
            flag=1
    
    return r+1+l+ (r*l)
    
for i in range(T):
    N=int(input())
    a=list(map(int,input().strip().split()))
    c=0
    b=[0]*N
    i=0
    for z in a:
        if z%2==0 and z%4!=0:
            b[i]=1
        elif z%4==0:
            b[i]=2
        i+=1
    #print(b)
    c=0
    for i in range(N):
        if b[i]==1:
            c+=zeroes(i)
    
    print(((N*(N+1))//2) - c)