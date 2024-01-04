import sys
input=sys.stdin.readline

n,m = map(int, input().split())
dp=[[0]+[-1e9]*m for _ in range(n+1)]
non_dp=[[0]+[-1e9]*m for _ in range(n+1)]

for i in range(1, n+1):
    num=int(input())
    for j in range(1, m+1):
        non_dp[i][j]=max(non_dp[i-1][j], dp[i-1][j])
        dp[i][j]=max(non_dp[i-1][j-1], dp[i-1][j])+num
print(max(dp[n][m], non_dp[n][m]))

