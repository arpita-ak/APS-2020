"""
Hackerrank miniMaxSum: https://www.hackerrank.com/challenges/mini-max-sum/problem
    
"""

def miniMaxSum(arr):
    res=[0,0]
    if min(arr)==max(arr):
            res[0]=res[1]=arr[0]*(len(arr)-1)
    else:
        for i in range(len(arr)):
            if arr[i]!=min(arr):
                res[1]+=arr[i]
            if arr[i]!=max(arr):
                res[0]+=arr[i]
    print(res[0],res[1])


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
