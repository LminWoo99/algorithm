import sys
input=sys.stdin.readline
m,n=map(int, input().split())
a=[list(map(int, input().split())) for _ in range(m)]
res=[]
dp=[[0]*(m+1) for _ in range(m+1)]
for i in range(1, m+1):
    for j in range(1, m+1):
        dp[i][j]=dp[i][j-1]+dp[i-1][j]-dp[i-1][j-1]+a[i-1][j-1]
for i in range(n):
    x1,y1,x2,y2=map(int, input().split())
    result=dp[x2][y2]-dp[x2][y1-1] -dp[x1-1][y2] + dp[x1-1][y1-1]
    res.append(result)
for i in res:
    print(i)
