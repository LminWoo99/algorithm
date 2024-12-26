import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))

dp = [0] * (n + 1)

for i in range(n):
    idx = data[i]
    dp[idx] = dp[idx - 1] + 1

print(n - max(dp))