import sys
input=sys.stdin.readline

a=input().rstrip()
l=len(a)

dp=[2500 for _ in range(l+1)]
dp[-1]=0
check=[[0]*l for _ in range(l)]

for i in range(l):
    check[i][i]=1

for i in range(1, l):
    if a[i]==a[i-1]:
        check[i-1][i]=1

for i in range(3, l+1):
    for start in range(l-i+1):
        end=start+i-1
        if a[start]==a[end] and check[start+1][end-1]:
            check[start][end]=1
for end in range(l):
    for start in range(end+1):
        if check[start][end]:
            dp[end]=min(dp[end], dp[start-1]+1)
        else:
            dp[end]=min(dp[end], dp[end-1]+1)

print(dp[l-1])