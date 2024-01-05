import sys
input=sys.stdin.readline

#i-> i, j,l
#v-> w

n,m=map(int, input().split())
wrong=input().rstrip()
answer=input().rstrip()

dp = [[i]+[0]*m for i in range(n+1)]
dp[0] = [i for i in range(m+1)]
for i in range(1, n+1):
    for j in range(1, m+1):
        dp[i][j]=min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])+1
        if wrong[i-1]==answer[j-1] or (wrong[i-1]=='v' and answer[j-1]=='w') or (wrong[i-1]=='i' and answer[j-1] in ['j','l']):
            dp[i][j]=dp[i-1][j-1]
print(dp[n][m])
