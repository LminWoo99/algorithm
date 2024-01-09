import sys
input=sys.stdin.readline

n,m=map(int, input().split())
active=list(map(int, input().split()))
cost=list(map(int, input().split()))
length=sum(cost)+1

dp=[[0]*length for _ in range(n+1)]
ans=10001
for i in range(1, n+1):
    cur_cost, cur_mem= cost[i-1], active[i-1]
    for j in range(length):
        dp[i][j]=dp[i-1][j]
    for j in range(cur_cost, length):
        dp[i][j]=max(cur_mem+dp[i-1][j-cur_cost], dp[i][j])
        if dp[i][j]>=m:
            ans=min(ans, j)
print(ans)