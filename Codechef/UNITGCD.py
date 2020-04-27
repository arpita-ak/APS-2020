"""
UNITGCD

"""

for i in range(int(input())):
    N=int(input())
    
    if N==1:
        print('1\n1 1')
        continue
    print(N//2)
    k=1
    if N%2==0:
        for z in range(N//2):
            print('2',k,k+1)
            k=k+2
    else:
        print('3 1',k+1,k+2)
        k=k+3
        for z in range(N//2 -1):
            print('2',k,k+1)
            k=k+2
            
        
        

   
    