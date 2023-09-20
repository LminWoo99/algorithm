def countWaysToColorHouses(n):
    mod = 10**9 + 7
    dp=[0]*(n+1)
    dp[2]=6
    if n==2:
        return dp[2]
    else:
        for i in range(4,n+1,2):
            dp[i]=dp[i-2]*3%mod
        return dp[n]
n = int(input().strip())
cnt=0
result = countWaysToColorHouses(n)
print(result)