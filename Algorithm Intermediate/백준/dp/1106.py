import sys
input=sys.stdin.readline

c,n = map(int, input().split())
dp=[sys.maxsize]*(c+100)
cost=[]
dp[0]=0
for i in range(n):
    x,y=map(int, input().split())
    cost.append((x,y))
for i in range(1, c+100):
    for j in range(n):
        dp[i]=min(dp[i], dp[i-cost[j][1]]+cost[j][0])

        
res=min(dp[c:])
print(res)