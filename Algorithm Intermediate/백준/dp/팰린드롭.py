import sys
input=sys.stdin.readline

n=int(input())
a=list(map(int, input().split()))
dp=[[0]*(n) for _ in range(n)]
for i in range(1, n):
    dp[i][i]=1
for i in range(n-1):
    if a[i]==a[i+1]:
        dp[i][i+1]=1
for cnt in range(n-2):
    for i in range(n-2-cnt):
        j= i+2+cnt
        if a[i]==a[j] and dp[i+1][j-1]==1:
            dp[i][j]=1

m=int(input())
for _ in range(m):
    x,y=map(int, input().split())
    print(dp[x-1][y-1])
