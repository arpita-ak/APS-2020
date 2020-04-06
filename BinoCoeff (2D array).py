
"""
Function to find Binomial Coefficients / Pascal Triangle elements / nCk using:
    1. Recursion (nk)
    2. DP using 2D array (nk) (Complete triangle can be accessed, once calculated)
    3. DP using 1D array (n) (Only particular row of the triangle can be accessed)

(2) is explained here    
"""

n=5
k=2

BinoCoeff = [[0]*(k+1) for i in range(n+1)]

for i in range(n+1):
    for j in range(min(i,k)+1):
        if j==0 or j==i:
            BinoCoeff[i][j] = 1
        else:
            BinoCoeff[i][j] = BinoCoeff[i-1][j-1] + BinoCoeff[i-1][j]
            
print(BinoCoeff[n][k])

