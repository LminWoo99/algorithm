import sys
n,k=map(int, sys.stdin.readline().split())
dp=[0]*(k+1)
dp[0]=1
for i in range(n):
    a=int(sys.stdin.readline())
    for j in range(a, k+1):
            dp[j]+=dp[j-a]
print(dp[k])
        
