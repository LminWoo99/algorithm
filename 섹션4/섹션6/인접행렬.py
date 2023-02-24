n,m=map(int, input().split())
a=[[0 for j in range(n)] for i in range(n)]
for i in range(m):
    row, col, path=map(int, input().split())
    a[row-1][col-1]=path
for j in range(n):
    for k in range(n):
        print(a[j][k], end=' ')
    print()

