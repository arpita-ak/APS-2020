"""
Viral Advertising:https://www.hackerrank.com/challenges/strange-advertising/problem

"""

m = 2
tot = 2
for _ in range(1, int(input())):
    m += m>>1
    tot += m
print(tot)
