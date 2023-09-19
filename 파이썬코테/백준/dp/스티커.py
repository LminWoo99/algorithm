t=int(input())
res=[]
for _ in range(t):
    n=int(input())
    a=[list(map(int, input().split())) for _ in range(2)]
    if n>1:
        a[0][1]+=a[1][0]
        a[1][1]+=a[0][0]
    for i in  range(2, n):
        a[0][i] += max(a[1][i-1], a[1][i-2])
        a[1][i] += max(a[0][i-1], a[0][i-2])
    print(max(a[0][n-1], a[1][n-1]))