"""
Left rotate the array of intergers

"""

def leftrotate(N,arr):
    temp=arr[0]
    for i in range(N-1):
        arr[i]=arr[i+1]
    arr[N-1]=temp
  
a=[1,2,3,4,5,6]
N=6
leftrotate(N,a)
print(a)

"""
Left rotate for the strings

"""

def leftrotate(k):
    k=k[1:]+k[0]
    return k

n='ABCDE'
print(leftrotate(n))

