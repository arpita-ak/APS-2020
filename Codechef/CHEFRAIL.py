"""
CHEFRAIL

"""

def distance(x,y):
    return (x**2+y**2)

def distanceXX(x1,x2):
    return (x1-x2)**2

T=int(input())

for z in range(T):
    F=list(map(int,input().strip().split()))    
    n=F[0]
    m=F[1]
    x=list(map(int,input().strip().split())) 
    y=list(map(int,input().strip().split())) 
    
    c=0
    for i in range(n):
        for j in range(i+1,n):
            d1=(x[i]-x[j])**2
            for k in range(m):
                d2=x[i]**2+y[k]**2
                d3=x[j]**2+y[k]**2
                if d1==d2+d3 or d2==d1+d3 or d3==d1+d2:
                    c+=1
    
    for i in range(m):
        for j in range(i+1,m):
            d1=(y[i]-y[j])**2
            for k in range(n):
                d2=y[i]**2+x[k]**2
                d3=y[j]**2+x[k]**2
                if d1==d2+d3 or d2==d1+d3 or d3==d1+d2:
                    c+=1
                
    print(c)