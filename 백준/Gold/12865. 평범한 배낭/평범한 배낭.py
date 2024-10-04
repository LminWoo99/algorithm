import sys
input=sys.stdin.readline

n,k=map(int, input().split())

dp=[[0]*(k+1) for _ in range(n+1)]

#보석
a=[]
for _ in range(n):
    x,y=map(int, input().split())
    a.append([x,y])
for i in range(1, n+1):
    cur_weight,cur_val=a[i-1][0],a[i-1][1]
    for j in range(1, k+1):
        if j<cur_weight:
            dp[i][j]=dp[i-1][j]
        else:
            dp[i][j]=max(dp[i-1][j], dp[i-1][j-cur_weight]+cur_val)
print(dp[-1][-1])