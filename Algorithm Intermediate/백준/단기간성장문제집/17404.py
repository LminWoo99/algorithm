import sys
input=sys.stdin.readline

n=int(input())
cost=[list(map(int, input().split())) for _ in range(n)]
INF=int(1e9)
res=INF
for i in range(3):
    dp=[[INF, INF, INF] for _ in range(n)]
    dp[0][i]=cost[0][i]
    for j in range(1,n):
        dp[j][0]=cost[j][0]+min(dp[j-1][1],dp[j-1][2])
        dp[j][1]=cost[j][1]+min(dp[j-1][0],dp[j-1][2])
        dp[j][2]=cost[j][2]+min(dp[j-1][0],dp[j-1][1])
    for j in range(3):
         if i!=j:
             res=min(res, dp[-1][j])
         
print(res)