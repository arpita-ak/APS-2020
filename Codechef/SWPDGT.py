"""
SWPDGT

"""

T=int(input())

for i in range(T):
    X=list(map(int,input().strip().split()))
    x=X[0]
    y=X[1]
    
    a=str(x)
    b=str(y)
    
    s=x+y
    
    if len(a)==len(b):
        if len(a)==1:
            print(s)
        else:
            s=max(s,int(a[0]+b[0])+int(a[1]+b[1]))
            s=max(s,int(a[0]+b[1])+int(b[0]+a[1]))
            s=max(s,int(b[0]+a[1])+int(a[0]+b[1]))
            s=max(s,int(b[0]+a[0])+int(b[1]+a[1]))
            print(s)
    else:
        if len(a)<len(b):
            a,b=b,a
            x,y=y,x
        s=max(s,int(a[0]+b[0])+int(a[1]))
        s=max(s,int(b[0]+a[1])+int(a[0]))
        print(s)

    