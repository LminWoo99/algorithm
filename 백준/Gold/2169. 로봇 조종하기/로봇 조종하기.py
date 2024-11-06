import sys  
input=sys.stdin.readline
n,m=map(int, input().split())

dp=[]
for _ in range(n):
    dp.append(list(map(int, input().split())))
for j in range(1, m):
    dp[0][j]+=dp[0][j-1]

for i in range(1, n):
    left=dp[i][:]
    right=dp[i][:]
    for j in range(m):
        if j==0:
            left[j]+=dp[i-1][j]
        else:
            left[j]+=max(dp[i-1][j],left[j-1])
    for j in range(m-1, -1, -1):
        if j==m-1:
            right[j]+=dp[i-1][j]
        else:
            right[j]+=max(dp[i-1][j], right[j+1])
    for j in range(m):
        dp[i][j]=max(left[j], right[j])
print(dp[-1][-1])
