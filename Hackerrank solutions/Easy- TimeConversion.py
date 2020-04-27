"""
Time Conversion: https://www.hackerrank.com/challenges/time-conversion/problem

"""

import os
import sys

def timeConversion(s):
    #print(s)
    if s[8]=='P':
        if (int(s[0])==1 and int(s[1])==2):
            s= s[0:8]
        else:
            t=str(int(s[0]+s[1])+12)
            s= t + s[2:8]
    elif s[8]=='A':
        if (int(s[0])==1 and int(s[1])==2):
            s='00'+s[2:8]
        else:
            s= s[0:8]

    
    print(s)
    return s
 
if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
