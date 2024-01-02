import sys
input=sys.stdin.readline
from collections import defaultdict,deque
n=int(input())
work=defaultdict(list)
dp=[0]*(n+1)
for i in range(n):
    sub=list(map(int, input().split()))
    if i!=0:
        dp[i+1]=sub[0]
        work[i+1]=sub[2:]
    else:
        dp[i+1]=sub[0]
for i in range(1, n+1):
    tmp=0
    index=0
    if work[i]:
        for work_time in work[i]:
            if tmp<dp[work_time]:
                
                tmp=max(tmp, dp[work_time])
                index=work_time
            # if dp[i]<dp[work_time]:
            # dp[i]+=dp[work_time]
        dp[i]+=dp[index]

print(max(dp))
        

    