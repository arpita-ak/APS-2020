s="Anagha"
l=len(s)
asc=""
for i in s:
    asc+=str(bin(ord(i))[2:])
    
print(asc)

 