
def solution(m, n, puddles):
    answer = []
    dp=[[0]*(m+1) for _ in range(n+1)]
    dp[1][1]=1
    for i in range(1, n+1):
        for j in range(1, m+1):
            if [j,i] in puddles or (i==1 and j==1):
                continue
            if i==1:
                dp[i][j]=dp[i][j-1]
            elif j==1:
                dp[i][j]=dp[i-1][j]
            else:
                dp[i][j]=dp[i-1][j]+dp[i][j-1]
    answer=dp[-1][-1]%1000000007
    return answer