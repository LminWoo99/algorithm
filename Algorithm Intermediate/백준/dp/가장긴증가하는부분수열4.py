import sys
input=sys.stdin.readline
n=int(input())
dp=[1]*(n+1)
a=list(map(int, input().split()))
for i in range(1, n):
    for j in range(i):
        if a[i]>a[j]:
            dp[i]=max(dp[i], dp[j]+1)

temp=[]            
print(max(dp))
result=max(dp)
for i in range(n-1, -1, -1):
    if dp[i]==result:
        temp.append(a[i])
        result -=1
temp.reverse()
print(*temp)