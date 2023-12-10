import sys
input=sys.stdin.readline

t=int(input())
dp=[0]*5001
dp[0]=1
for n in range(2, 5001, 2):
    for i in range(2, n+1, 2):
        dp[n] += dp[i-2] * dp[n-i]
    dp[n] %= 1000000007
for _ in range(t):
    print(dp[int(input())])