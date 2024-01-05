import sys
input=sys.stdin.readline

n=int(input())
a=[]
for _ in range(n):
    r,c=map(int, input().split())
    a.append((r,c))
dp=[[0]*n for _ in range(n)]

for term in range(1, n):
    for start in range(n):
        if start+term==n:
            break
        dp[start][start+term]=sys.maxsize
        for t in range(start, start+term):
            dp[start][start+term]=min(dp[start][start+term], dp[start][t]+dp[t+1][start+term]+a[start][0]*a[t][1]*a[start+term][1])
print(dp[0][n-1])