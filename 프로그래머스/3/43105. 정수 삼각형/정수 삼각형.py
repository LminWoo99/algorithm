
def solution(triangle):
    dp=[[0]*(i+1) for i in range(501)]
    dp[0][0]=triangle[0][0]
    ## 첫번쨰가지에서 출발
    n=len(triangle)
    for i in range(1, n):
        for j in range(i+1):
            if j==0:
                dp[i][j]=dp[i-1][j]+triangle[i][j]
            elif j==i:
                dp[i][j]=dp[i-1][j-1]+triangle[i][j]
            else:
                dp[i][j]=max((dp[i-1][j-1]+triangle[i][j]), (dp[i-1][j]+triangle[i][j]))
    answer=max(dp[n-1])
    return answer   