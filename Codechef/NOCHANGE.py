"""
NOCHANGE

"""

T=int(input())

def checkforNO(N,rd,Z):
    flag=0
    for i in range(N):
        if Z%rd[i]==0:
            Z=rd[i]
        else:
            flag=1
    if flag==0:
        return True
    else:
        return False
 

for z in range(T):
    n=list(map(int,input().strip().split()))
    N=n[0]
    P=n[1]
    Z=P
    Y=0
    D=list(map(int,input().strip().split())) 
    
    rd=D[::-1]
    
    q=[0]*N
    Q=0
    flag=1

    check=0
    
    if rd[0]>Z:
        q[0]=1
        check=2
    elif checkforNO(N,rd,Z)==True:
        flag=0
        check=1
    
    if flag==0:
            print('NO')
            check=1
        
    if check==0:
        for i in range(N):
            m=P%rd[i]
            if m==0:
                if checkforNO(N-i,rd[i:],Z)==True and check!=2:
                    q[i-1]+=1
                    check=2
                if check!=2:
                    Q= P//rd[i]
                    P=P-(Q-1)*rd[i]
                    Y=Y+(Q-1)*rd[i]
                    q[i]=Q-1
            else:
                if check!=2:
                    Q= P//rd[i]
                    P=P-(Q)*rd[i]
                    Y=Y+(Q)*rd[i]
                    q[i]=Q
                
            if i==N-1 and check!=2:
                while(P>0):
                    P=P-rd[i]
                    Y=Y+rd[i]
                    if Y==Z:
                        q[i-1]+=1
                    elif Y>Z:
                        q[i]+=1
                    check=2
    if check==2:
        print('YES ',end='')
        div=q[::-1]
        for i in range(N):
            print(div[i],end=' ')
        print('')