import sys
input=sys.stdin.readline

n=int(input())
a=list(map(int, input().split()))
dp=[0]*(n)
for i in range(n):
    dp[i]=max(a[i], dp[i-1]+a[i])

print(max(dp))