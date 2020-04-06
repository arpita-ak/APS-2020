"""
Generates all possible Permutations

"""
def toString(List): 
	return ''.join(List) 

def permute(a, l, r): 
	if l == r: 
		permu.append(toString(a) )
	else: 
		for i in range(l, r+1): 
			a[l], a[i] = a[i], a[l] 
			permute(a, l + 1, r) 
			a[l], a[i] = a[i], a[l] # backtrack 

def generate_permutations(string,n):
    a = list(string) 
    permute(a, 0, n-1) 

s = "0123"
permu=[]
generate_permutations(s,len(s))
print(permu)