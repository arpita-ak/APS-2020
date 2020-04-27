"""
CNOTE: https://www.codechef.com/problems/CNOTE
    
"""

for _ in range(int(input())):
	p=[]
	c=[]
	x,y,k,n=map(int,input().split())
	for i in range(n):
		page,cost=map(int,input().split())
		p.append(page)
		c.append(cost)
	needed=x-y
	for j in range(n):
		if needed<=p[j] and k>=c[j]:
			print('LuckyChef')
			break
	else:
		print('UnluckyChef')


   
    