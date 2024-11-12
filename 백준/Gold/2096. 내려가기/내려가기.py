import sys
input=sys.stdin.readline
n=int(input())
board=list(map(int, input().split()))

min_dp=board
max_dp=board
for i in range(n-1):
    board=list(map(int, input().split()))
    max_dp=[board[0]+max(max_dp[0],max_dp[1]), board[1]+max(max_dp[0],max_dp[1], max_dp[2]) , board[2]+max(max_dp[1],max_dp[2])]
    min_dp=[board[0]+min(min_dp[0],min_dp[1]), board[1]+min(min_dp[0],min_dp[1], min_dp[2]) , board[2]+min(min_dp[1],min_dp[2])]
print(max(max_dp), min(min_dp))