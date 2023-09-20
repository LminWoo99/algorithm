import sys
n=int(sys.stdin.readline())
a=list(map(int, sys.stdin.readline().split()))
dp=[1]*n
dp2=[1]*n
for i in range(n):
    for j in range(i):
        if a[i]>a[j]:
            dp[i]=max(dp[j]+1, dp[i])
for i in range(n-1, -1, -1):
    for j in range(n-1, i, -1):
        if a[i]>a[j]:
            dp2[i]=max(dp2[j]+1, dp2[i])
result=[0 for i in range(n)]
for i in range(n):
    result[i]=dp[i]+dp2[i]-1
print(max(result))
    