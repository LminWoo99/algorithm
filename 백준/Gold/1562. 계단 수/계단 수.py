import sys
input=sys.stdin.readline

n=int(input())
num_range=10
bit_range=1<<num_range
MOD=10**9

dp=[[[0]*(bit_range) for _ in range(num_range)] for _ in range(n+1)]


for k in range(num_range):
    dp[1][k][1<<k]=1
for i in range(1, n):
    for j in range(num_range):
        for k in range(bit_range):
            if 0<=j<9:
                dp[i+1][j+1][k|1<<(j+1)] += dp[i][j][k]
                dp[i+1][j+1][k|1<<(j+1)] %= MOD
            if 0<j<=9:
                dp[i+1][j-1][k|1<<(j-1)] += dp[i][j][k]
                dp[i+1][j-1][k|1<<(j-1)] %= MOD
res=0
for k in range(1, num_range):
    res+=dp[n][k][1023]
    res%=MOD
print(res)    