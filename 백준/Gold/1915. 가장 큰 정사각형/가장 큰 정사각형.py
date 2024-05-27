import sys
input=sys.stdin.readline

n,m=map(int, input().split())
board=[list(map(int, input().rstrip())) for _ in range(n)]


dp=[[0]*(m+1) for _ in range(n+1)]
max_side=0
if n==1 or m==1:
    print(1)
else:
    for i in range(m):
        dp[0][i]=board[0][i]
    for i in range(1, n+1):
        for j in range(1, m+1):
            if board[i-1][j-1]==1:
                dp[i][j]=min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])+1
                max_side=max(max_side, dp[i][j])
    print(max_side*max_side)
            