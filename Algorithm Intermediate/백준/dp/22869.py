import sys
input=sys.stdin.readline

n,k=map(int, input().split())
a=list(map(int, input().split()))
dp=[0]*n
dp[0]=1
for i in range(n-1):
    for j in range(i+1, n):
        if dp[i] and (j-i)*(1+abs(a[i]-a[j])) <=k:
            dp[j]=1

print("YES" if dp[n-1] else "NO")