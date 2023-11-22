# import sys
# input=sys.stdin.readline
import time
start=time.time()
n=int(input())
a=[]
for i in range(n):
    x,y=map(int, input().split())
    a.append((x,y))
dp=[0]*(n+1)

for i in range(1,n+1):
    dp[i] = max(dp[i], dp[i - 1])
    j=a[i-1][0]
    if i+j<=n+1:
        dp[i+j-1]=max(dp[i+j-1], dp[i-1]+a[i-1][1])

print(dp[-1])
end=time.time()
print(end-start)
