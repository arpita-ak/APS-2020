"""
HS08TEST

"""

X=list(map(float,input().strip().split()))

b=X[1]

w=X[0]

if w+0.5>b or w%5!=0:
    print(b,end='')
    print(0)
else:
    print(b-w-0.50,end='')
    print(0)
    