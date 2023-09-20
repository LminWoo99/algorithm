n,m=map(int, input().split())
a=[0]*(n+1)
for i in range(1, n+1):
    a[i]=i
for x in range(m):
    d, e=map(int , input().split())
    a[d],a[e]=a[e],a[d]
for i in range(1, n+1):
    print(a[i], end=' ')