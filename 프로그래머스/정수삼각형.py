import itertools
def solution(triangle):
    answer = 0
    n=len(triangle)
    dp=[[0]*(i+1) for i in range(501)]
    dp[0][0]=triangle[0][0]
    for i in range(1, n):
        for j in range(len(triangle[i])):
            if j!=0 and j!=i:
                dp[i][j]=max(dp[i-1][j-1]+triangle[i][j], dp[i-1][j]+triangle[i][j])
            elif j==0:
                dp[i][j]=dp[i-1][0]+triangle[i][j]
            else:
                dp[i][j]=dp[i-1][j-1]+triangle[i][j]
    answer=max(dp[n-1])
    
    return answer