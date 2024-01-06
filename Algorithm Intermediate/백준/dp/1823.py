import sys
input=sys.stdin.readline

n=int(input())
a=[0]
for _ in range(n):
    x=int(input())
    a.append(x)
dp = [[a[i] * n  if i == j else 0 for i in range(n + 1)] for j in range(n + 1)]
for left in range(1, n + 1):
    for right in range(left - 1, 0, -1):
        dp[right][left] = max(dp[right + 1][left] + a[right] * (n - left + right), dp[right][left - 1] + a[left]*(n - left + right))

print(dp[1][n])