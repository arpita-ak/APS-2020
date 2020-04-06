
"""
Function to find Binomial Coefficients / Pascal Triangle elements / nCk using:
    1. Recursion (nk)
    2. DP using 2D array (nk) (Complete triangle can be accessed, once calculated)
    3. DP using 1D array (n) (Only particular row of the triangle can be accessed) (auxiliary space: O(n))
    
(3) is explained here

"""

n=5
k=2

BinoCoeff = [0]*(n+2)

for i in range(n+2):
    for j in range(i,0,-1):
        if j==0 or j==i:
            BinoCoeff[j] = 1
        else:
            BinoCoeff[j] = BinoCoeff[j-1] + BinoCoeff[j]
    
print(BinoCoeff[k+1])
