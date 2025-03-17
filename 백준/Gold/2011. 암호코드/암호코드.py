import sys
input=sys.stdin.readline
a=input().rstrip()

dp=[0]*(len(a)+1)
dp[0]=1
for i in range(1, len(a)+1):
    if i>=2 and not int(a[i-2:i]):
        dp[-1]=0
        break
    if int(a[i-1]):
        dp[i]+=dp[i-1]
    if i>=2:
        if a[i-2]!='0' and int(a[i-2:i])<27:
            dp[i]+=dp[i-2]
print(dp[-1]%1000000)