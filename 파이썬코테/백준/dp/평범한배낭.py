import sys
n,k=map(int, sys.stdin.readline().split())
dp=[[0]*(k+1) for _ in range(n+1)]
tmp=[[0,0]]
for i in range(n):
    w, v=map(int, sys.stdin.readline().split())
    tmp.append([w,v])
for i in range(1, n+1):
    for j in range(1, k+1):
        w,v=tmp[i]
        if w<=j:
            dp[i][j]=max(dp[i-1][j], dp[i-1][j-w]+v)
        else:
            dp[i][j]=dp[i-1][j]
    
print(dp[-1][-1])