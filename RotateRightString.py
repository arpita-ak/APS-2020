'''
Using strings
'''
def rightrotate(n):
    k=str(n)
    l=len(k)
    last=k[l-1]
    k=last+k[0:l-1]
    return k

n='ABCDE'
print(rightrotate(n))


'''
Rotates right : Integer

'''
import math

def rightrotate(n):
    dig=math.ceil(math.log10(n))
    r=n%10
    n=n//10
    r=r*pow(10,dig-1)
    return r+n

n=1234
print(rightrotate(n))
