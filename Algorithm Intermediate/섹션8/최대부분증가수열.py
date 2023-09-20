n=int(input())
a=list(map(int, input().split()))
a.insert(0,0)
d=[0]*(n+1)
d[1]=1
res=0

for i in range(2, n+1):
    max=0
    for j in range(i-1, 0, -1):
        if a[j]<a[i] and max<d[j]:
            max=d[j]
    d[i]=max+1
    if res<d[i]:
        res=d[i]
print(res)