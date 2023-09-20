n=int(input())
dp=[0]*(n+1)
tmp=[]
for i in range(n):
    tmp.append(list(map(int, input().split())))
for i in range(n-1, -1, -1):
    if i+tmp[i][0]>n:
        dp[i]=dp[i+1]
    else:
        dp[i]=max(tmp[i][1]+dp[i+tmp[i][0]], dp[i+1])
print(dp[0])
        
