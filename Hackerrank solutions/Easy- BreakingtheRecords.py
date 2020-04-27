"""
Breaking the Records: https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem

"""
import os

def breakingRecords(n,scores):
    mini=scores[0]
    count=[0,0]
    maxi=scores[0]
    
    for i in range(n):
        if scores[i]<mini:
            mini=scores[i]
            count[1]=count[1]+1
        if scores[i]>maxi:
            maxi=scores[i]
            count[0]=count[0]+1
    print(count)
    return count
    
fptr = open(os.environ['OUTPUT_PATH'], 'w')

n = int(input())

scores = list(map(int, input().rstrip().split()))

result = breakingRecords(n,scores)

fptr.write(' '.join(map(str, result)))
fptr.write('\n')

fptr.close()
