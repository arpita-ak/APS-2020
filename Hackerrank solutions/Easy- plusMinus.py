"""
Hackerrank plusMinus: https://www.hackerrank.com/challenges/plus-minus/problem
    
"""

def plusMinus(arr):
    res=[0,0,0]
    n=len(arr)
    for i in range(n):
        if arr[i]>0:
            res[0]+=1
        if arr[i]<0:
            res[1]+=1
        if arr[i]==0:
            res[2]+=1
    for i in range(3):
        print(round(res[i]/n, 6))
    
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
