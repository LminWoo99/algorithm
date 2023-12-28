import sys
input=sys.stdin.readline

n=int(input())
a=list(map(int, input().split()))
dp=[0]*n
dp=a[:]
for i in range(1, n):
    for j in range(i):
        if a[j]<a[i]:
            dp[i]=max(dp[i], a[i]+dp[j])
print(max(dp))