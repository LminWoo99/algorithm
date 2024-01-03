import sys
input=sys.stdin.readline

n,m = map(int, input().split())
plane=[list(map(int, input().split())) for _ in range(n)]

dp_up=[[-1e9]*(m) for _ in range(n)]
dp_down=[[-1e9]*(m) for _ in range(n)]
dp_up[n-1][0]=plane[n-1][0]
dp_down[n-1][m-1]=plane[n-1][m-1]
for i in range(n-1, -1, -1):
    for j in range(m):
        if i==n-1 and j==0:
            continue
        if i<n-1:
            dp_up[i][j]=max(dp_up[i][j], dp_up[i+1][j])
        if j>0:
            dp_up[i][j]=max(dp_up[i][j], dp_up[i][j-1])
        dp_up[i][j]+=plane[i][j]
for i in range(n-1, -1, -1):
    for j in range(m-1, -1, -1):
        if i==n-1 and j==m-1:
            continue
        if i<n-1:
            dp_down[i][j]=max(dp_down[i][j], dp_down[i+1][j])
        if j<m-1:
            dp_down[i][j]=max(dp_down[i][j], dp_down[i][j+1])
        dp_down[i][j]+=plane[i][j]
result=-1e9
for i in range(n):
    for j in range(m):
        result=max(result, dp_up[i][j]+dp_down[i][j])
print(result)