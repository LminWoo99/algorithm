import sys
input=sys.stdin.readline


n=int(input())
dp=[1000001]*(n+1)
a=list(map(int, input().split()))
dp[0]=0
for i in range(1, n+1):
    for j in range(1, i+1):
        dp[i]=min(dp[i], dp[i-j]+a[j-1])
print(dp[-1])