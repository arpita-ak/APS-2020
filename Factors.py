
"""
Gives the factors of the given number

"""

def factors(n):
    f=[]
    for i in range(1,n):
        if n%i==0:
            f.append(i)
    return f

n=10
f=factors(n)
print(f)