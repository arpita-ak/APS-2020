"""
ADASHOP2

"""

T=int(input())

a=[[1,1],[2,2],[3,1],[1,3],[2,4],[1,5],[5,1],[6,2],[7,1],[1,7],[2,8],[8,2],[7,3],[8,4],[4,8],[5,7],[6,8],[8,6],[7,7],[8,8]]

for i in range(T):
    X=list(map(int,input().strip().split()))
    r0=X[0]
    c0=X[1]
    l=len(a)
    
    if r0==1 and c0==1:
        print(l)
        for i in range(l):
            print(a[i][0],a[i][1])
            
    else:
        print(l+2)
        print(r0,c0)
        av=(r0+c0)//2
        
        print(av,av)
        for i in range(l):
            print(a[i][0],a[i][1])
    
    
   
    