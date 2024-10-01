import sys
input=sys.stdin.readline

n,k=map(int, input().split())
# 물건 리스트
a=[[0,0]]
for _ in range(n):
    x,y=map(int, input().split())
    a.append([x,y])
dp=[[0]*(k+1) for _ in range(n+1)]
a.sort()
for i in range(1, n+1):
    for j in range(1, k+1):
        w,v=a[i]
        if j<w:
            dp[i][j]=dp[i-1][j]
        else:
            dp[i][j]=max(dp[i-1][j], dp[i-1][j-w]+v)
print(max(map(max, dp)))