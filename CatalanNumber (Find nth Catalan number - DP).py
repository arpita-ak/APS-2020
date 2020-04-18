def factorial(k):
    return allfact[k]

def nthCatalanNumber(n):
    return factorial(2*n)//(factorial(n+1)*factorial(n))

n=5
allfact=[]
allfact.append(1)
for i in range(1,2*n +1):
    allfact.append(i*allfact[i-1])
    
print(nthCatalanNumber(n))  
