import sys
input=sys.stdin.readline

t=int(input())
k=int(input())
coins=[]
for i in range(k):
    p, n=map(int, input().split())
    coins.append((p,n))
dp=[0]*(t+1)
dp[0]=1
for coin, cnt in coins:
    for money in range(t, 0 , -1):
        for i in range(1, cnt+1):
            if money-coin*i>=0:
                dp[money]+=dp[money-i*coin]

print(dp[t])