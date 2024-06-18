import sys
input=sys.stdin.readline

n=int(input())
counsel_list=[]
for _ in range(n):
    t,p=map(int, input().split())
    counsel_list.append([t,p])
dp=[0]*(n+2)
for i in range(1, n+1):
    dp[i]=max(dp[i], dp[i-1])
    if i+counsel_list[i-1][0]<=n+1:
        dp[i+counsel_list[i-1][0]]=max(dp[i+counsel_list[i-1][0]], dp[i]+counsel_list[i-1][1])
    
print(max(dp))