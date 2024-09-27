import sys
input=sys.stdin.readline

n=int(input())
p=list(map(int, input().split()))
dp=[0]*(n+1)
for i in range(1, n+1):
    dp[i]=p[i-1]
    
for i in range(1, n+1):
    for j in range(1, i):
        dp[i]=max(dp[i], dp[j]+p[i-j-1])
print(dp[-1])