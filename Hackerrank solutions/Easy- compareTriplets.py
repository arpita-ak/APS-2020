"""
Hackerrank compareTriplets: https://www.hackerrank.com/challenges/compare-the-triplets/problem
    
"""
import os

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    s=[0,0]
    for i in range(3):
        if a[i]>b[i]:
            s[0]+=1
        elif a[i]<b[i]:
            s[1]+=1
        elif a[i]==b[i]:
            s[0]+=0
    return s


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
