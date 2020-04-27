"""
THEATRE

"""

import numpy as np

permu=[]

def toString(List): 
	return ''.join(List) 

def permute(a, l, r): 
	if l == r: 
		permu.append(toString(a) )
	else: 
		for i in range(l, r+1): 
			a[l], a[i] = a[i], a[l] 
			permute(a, l + 1, r) 
			a[l], a[i] = a[i], a[l] # backtrack 

def generate_permutations(string,n):
    a = list(string) 
    permute(a, 0, n-1) 

T=int(input())

total=0

for i in range(T):
    
    N=int(input())
    mov=np.zeros([4,4])
    for j in range(N):
        X=list(map(str,input().strip().split()))
        
        if X[0]=='A' and X[1]=='12':
            mov[0][0]+=1
        elif X[0]=='A' and X[1]=='3':
            mov[0][1]+=1
        elif X[0]=='A' and X[1]=='6':
            mov[0][2]+=1
        elif X[0]=='A' and X[1]=='9':
            mov[0][3]+=1
            
            
        elif X[0]=='B' and X[1]=='12':
            mov[1][0]+=1
        elif X[0]=='B' and X[1]=='3':
            mov[1][1]+=1
        elif X[0]=='B' and X[1]=='6':
            mov[1][2]+=1
        elif X[0]=='B' and X[1]=='9':
            mov[1][3]+=1
            
        elif X[0]=='C' and X[1]=='12':
            mov[2][0]+=1
        elif X[0]=='C' and X[1]=='3':
            mov[2][1]+=1
        elif X[0]=='C' and X[1]=='6':
            mov[2][2]+=1
        elif X[0]=='C' and X[1]=='9':
            mov[2][3]+=1
            
        elif X[0]=='D' and X[1]=='12':
            mov[3][0]+=1
        elif X[0]=='D' and X[1]=='3':
            mov[3][1]+=1
        elif X[0]=='D' and X[1]=='6':
            mov[3][2]+=1
        elif X[0]=='D' and X[1]=='9':
            mov[3][3]+=1
            
    #print(mov)
    
    
    s = "0123"
    generate_permutations(s,len(s))
    
    #print(permu)
    cost=[]
    
    for iteri in range(24):
        temp=0
        order=int(permu[iteri])
        nin=order%10
        order=order//10
        six=order%10
        order=order//10
        th=order%10
        order=order//10
        tw=order%10
        order=order//10
        
        o=[tw,th,six,nin]
        
        new=[]
        for z in range(4):
            h=o[z]
            new.append(mov[h][z])
        
        d=[100,75,50,25]
        
        c=0
        for z in range(4):
            if new[z]==0:
                c+=1
        new.sort(reverse=True)
        
        for z in range(4):
            temp+=new[z]*d[z]
        temp-=c*100
        cost.append(temp)
    
        #print(new)
    maxi=int(max(cost))
    print(maxi)
    total=total+maxi
print(total)