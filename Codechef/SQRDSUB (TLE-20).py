"""
SQRDSUB

"""
T=int(input())

def good(n):
    if n%2==0:
        if (n//2)%2==0:
            return 1
        else:
            return 0
    else:
        return 1

for i in range(T):
    N=int(input())
    a=list(map(int,input().strip().split()))
    c=0
    for i in range(N):
        pro=1
        for z in range(i,N):
            pro*=a[z]
            if good(pro)==1:
                #print(pro)
                c+=1
    print(c)        