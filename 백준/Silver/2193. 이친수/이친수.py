import sys
input=sys.stdin.readline

n=int(input())
dp=[0]*91
dp[1]=1
dp[2]=1
dp[3]=2
if n<=3:
    print(dp[n])
else:
    for i in range(3, n+1):
        dp[i]=dp[i-2]+dp[i-1]
    print(dp[n])