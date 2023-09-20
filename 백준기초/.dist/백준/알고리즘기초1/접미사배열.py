a=input()
res=[]
for i in range(len(a)):
    tmp=a[i:len(a)+1]
    res.append(tmp)
res.sort()
for i in res:
    print(i)