import sys
input=sys.stdin.readline

n=int(input())
a=[]
dp=[1]*n
for i in range(n):
    x,y=map(int, input().split())
    a.append([x,y])
a.sort()
for i in range(1, n):
    for j in range(i):
        if a[i][1]>a[j][1]:
            dp[i]=max(dp[i], dp[j]+1)
print(n-max(dp))