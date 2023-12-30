import sys
input=sys.stdin.readline

n=int(input())
a=list(map(int, input().split()))


dp=[[0]*21 for _ in range(n)]
dp[0][a[0]]+=1

for i in range(1, n-1):
    for j in range(len(dp[i])):
        if dp[i-1][j]!=0:
            plus=j+a[i]
            minus=j-a[i]
            if 0<=plus<21:
                dp[i][plus]+=dp[i-1][j]
            if 0<=minus<21:
                dp[i][minus]+=dp[i-1][j]
print(dp[n-2][a[-1]])