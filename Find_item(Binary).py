def find_item(l,item):
    l.sort()
    if len(l)==0:
        return False
    m=len(l)//2
    if l[m]==item:
        return True

    if item<l[m]:
        return find_item(l[:m],item)
    else:
        return find_item(l[m+1:],item)
    
    return True
    
l=['parker','drew','cameron','logan','alex','chris']
i=l[0]
print(find_item(l,i))
i="Tensor"
print(find_item(l,i))
i=l[4]
print(find_item(l,i))
i='juice'
print(find_item(l,i))