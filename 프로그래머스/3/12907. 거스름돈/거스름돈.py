def solution(n, money):
    dp=[0]*(n+1)
    dp[0]=1
    for i in money:
        for price in range(i, n+1):
            dp[price]+=dp[price-i]
    return dp[-1]%1000000007


