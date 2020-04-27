"""
GIFTSRC

"""
T=int(input())

def issame(i,f):
    if (i=='U' and f=='R') or (i=='D' and f=='R') or  (i=='U' and f=='L') or  (i=='D' and f=='L') or (f=='U' and i=='R') or (f=='D' and i=='R') or  (f=='U' and i=='L') or  (f=='D' and i=='L'):
        return 0
    else:
        return 1


for j in range(T):
    N=int(input())
    k=input()
    x=0
    y=0
    i=0
    if k[i]=='L':
            x-=1
    elif k[i]=='R':
            x+=1
    elif k[i]=='U':
            y+=1
    elif k[i]=='D':
            y-=1
            
    for i in range(1,N):
        if issame(k[i],k[i-1])==1:
            continue
        else:
            if k[i]=='L':
                x-=1
            elif k[i]=='R':
                x+=1
            elif k[i]=='U':
                y+=1
            elif k[i]=='D':
                y-=1
                
    print(x,y)
    
            

   
    