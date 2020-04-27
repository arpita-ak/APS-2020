"""
LECANDY

"""

n=int(input())

for i in range(n):
    k=list(map(int,input().strip().split()))
    can=list(map(int,input().strip().split()))
    if k[1]>=sum(can):
        print("Yes")
    else:
        print("No")
