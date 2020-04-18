def factorial(k):
    if k==0:
        return 1
    return k*factorial(k-1)

def nthCatalanNumber(n):
    return factorial(2*n)//(factorial(n+1)*factorial(n))

n=5
print(nthCatalanNumber(n))  
