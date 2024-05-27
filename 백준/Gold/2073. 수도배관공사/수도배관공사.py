import sys
input=sys.stdin.readline

d,p=map(int, input().split())
pipes=[]


dp=[0]*(d+1)
dp[0]=sys.maxsize
tmp=0
for _ in range(p):
    l,c=map(int, input().split())
    max_dp=dp.copy()
    for i in range(l, d+1):
        if max_dp[i-l]:
            dp[i]=max(dp[i], min(max_dp[i-l], c))

print(dp[-1])
        
    



