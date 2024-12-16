import sys
input=sys.stdin.readline

a=input().rstrip()
dp=[0]*(len(a)+1)
if a[0]=='0':
    print(0)
else:
    dp[0]=dp[1]=1
    for i in range(2, len(a)+1):
        if int(a[i-1])>0:
            dp[i]+=dp[i-1]
        tmp=int(a[i-2]+a[i-1])
        if tmp>=10 and tmp<=26:
            dp[i]+=dp[i-2]
    print(dp[-1]%1000000)