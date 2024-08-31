def solution(money):
    answer = 0
    n=len(money)
    dp=[0]*(n+1)
    dp2=[0]*(n+1)
    for i in range(1, n):
        dp[i]=max(dp[i-2]+money[i-1], dp[i-1])
    for i in range(2, n+1):
        dp2[i]=max(dp2[i-2]+money[i-1], dp2[i-1])
    answer=max(max(dp), max(dp2))
    return answer