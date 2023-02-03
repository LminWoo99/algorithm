a=input()
b=input()
ah=dict()
bh=dict()
for x in a:
    if ah.get(x, 0)==0:
        ah[x]=1
    else:
        temp=ah.get(x)
        ah[x]=temp+1
print(ah)
for x in b:
    if bh.get(x, 0)==0:
        bh[x]=1
    else:
        temp=bh.get(x)
        bh[x]=temp+1
if ah==bh:
    print("yes")
else:
    print("no")
    

    