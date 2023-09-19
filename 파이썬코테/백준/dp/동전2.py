import sys
input=sys.stdin.readline
n,k=map(int, input().split())
dp=[99999]*(k+1)
res=[]
for _ in range(n):
    tmp=int(input())
    for i in range(1, k+1):
        if i>=tmp:
            if i%tmp==0:
                dp[i]=min(i//tmp, dp[i-tmp]+dp[tmp], dp[i])
            else:
                dp[i]=min(dp[i-tmp]+dp[tmp], dp[i])
if dp[k]==99999:
    print(-1)
else:
    print(dp[k])

