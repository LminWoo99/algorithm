import sys
input=sys.stdin.readline

a=input().rstrip()
b=input().rstrip()
dp=[[""]*(len(b)+1) for _ in range(len(a)+1)]
for i in range(1, len(a)+1):
    for j in range(1, len(b)+1):
        if a[i-1]==b[j-1]:
            dp[i][j]=dp[i-1][j-1]+a[i-1]
            continue
        if len(dp[i][j-1])>=len(dp[i-1][j]):
            dp[i][j]=dp[i][j-1]
        else:
            dp[i][j]=dp[i-1][j]
print(len(dp[-1][-1]))
print(dp[-1][-1])