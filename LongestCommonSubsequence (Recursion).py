def LongestCommonSubsequence(s1,s2,i,j):
    if i==0 or j==0:
        return 0
    if s1[i-1]==s2[j-1]:
        k=LongestCommonSubsequence(s1,s2,i-1,j-1)
        return k+1
    else:
        k=max( LongestCommonSubsequence(s1,s2,i-1,j), LongestCommonSubsequence(s1,s2,i,j-1))
        return k
    
s1 = "abcda"
s2 = "bdabac"
l1 = len(s1) #cols
l2 = len(s2) #rows
k = LongestCommonSubsequence(s1,s2,l1,l2)
print(k)
