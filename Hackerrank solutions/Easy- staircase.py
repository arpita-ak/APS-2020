"""
Hackerrank staircase: https://www.hackerrank.com/challenges/staircase/problem
    
"""

def staircase(n):
    for m in range(n):
        print((n - m - 1) * ' ' + (m + 1) * '#')

if __name__ == '__main__':
    n = int(input())

    staircase(n)
