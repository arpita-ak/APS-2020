"""
Function to find Binomial Coefficients / Pascal Triangle elements / nCk using:
    1. Recursion (nk)
    2. DP using 2D array (nk) (Complete triangle can be accessed, once calculated)
    3. DP using 1D array (n) (Only particular row of the triangle can be accessed)
    
(1) is written here

"""
n=5
k=2

def BinoCoeff(n,k):
    if k==0 or k==n:
        return 1
    return BinoCoeff(n-1,k-1) + BinoCoeff(n-1,k)

print(BinoCoeff(n,k))