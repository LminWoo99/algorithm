import sys
input=sys.stdin.readline

n,m,h=map(int, input().split())
dp=[0]*(h+1)
a=[]
dp[0]=1
for i in range(n):
    tmp=list(map(int, input().split()))
    a.append(tmp)
for i in range(len(a)):
    for j in range(h, 0, -1):
        for k in range(len(a[i])):
            if j-a[i][k]>=0:
                dp[j]+=dp[j-a[i][k]]
print(dp[-1]%10007)