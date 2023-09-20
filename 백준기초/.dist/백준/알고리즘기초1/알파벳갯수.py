a=input()
res=[0]*26
for i in a:
    tmp=ord(i)-97
    res[tmp]+=1
print(*res)
