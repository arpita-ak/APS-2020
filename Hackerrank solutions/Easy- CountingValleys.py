"""
CountingValleys: https://www.hackerrank.com/challenges/counting-valleys/problem

"""

import os

# Complete the countingValleys function below.
def countingValleys(n, s):
    c=0
    countvalleys=0
    for i in range(n):
        #print(c)
        if s[i]=='U':
            c+=1
            if c==0:
                countvalleys+=1
                #print(countvalleys)
        if s[i]=='D':
            c-=1
    return(countvalleys)
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
