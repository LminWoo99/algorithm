import sys
input=sys.stdin.readline

t=int(input())
INF = sys.maxsize
dp = [INF for _ in range(101)]
dp[2] = 1
dp[3] = 7
dp[4] = 4
dp[5] = 2
dp[6] = 6
dp[7] = 8
dp[8] = 10
for i in range(9, 101):
    for j in range(2, 8):
        if j!=6:
            dp[i]=min(dp[i], dp[i-j]*10+dp[j])
        else:
            dp[i]=min(dp[i], dp[i-j]*10)
for _ in range(t):
    n=int(input())
    max_res=('7' if n%2 else '1')+'1'*(n//2-1)
    print(dp[n], max_res)
    