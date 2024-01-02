import sys
input=sys.stdin.readline

n=int(input())
kids=[0]
for _ in range(n):
    kid=int(input())
    kids.append(kid)

dp=[1]*(n+1)
tmp=0
tmp_index=0
for i in range(1, n+1):
    for j in range(1,i):
        if kids[j]<kids[i]:
            dp[i]=max(dp[i],dp[j]+1)
print(n-max(dp))

