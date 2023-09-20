n, m=map(int, input().split())
res=[0]*(n+1)
for i in range(1,n+1):
    res[i]=i
for i in range(m):
    a,b,c=map(int, input().split())
    temp=res[c:b+1]+res[a:c]
    res[a:b+1]=temp
for i in range(1,n+1):
    print(res[i], end=' ')
    