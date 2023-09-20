a=[]
avg=0
for i in range(5):
    tmp=int(input())
    a.append(tmp)
    avg+=tmp
a=sorted(a)
print(avg//5)
print(a[2])