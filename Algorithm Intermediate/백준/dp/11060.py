import sys
input=sys.stdin.readline
from collections import deque

def BFS(x):
    dq=deque()
    dq.append(x)
    dp[x]=0
    while dq:
        x=dq.popleft()
        if x==n:
            return dp[x]
        else:
            for i in range(1,jump[x-1]+1):
                xx=x+i
                if 1<=xx<=n and visit[xx]!=1:
                    dp[xx]=min(dp[x]+1, dp[xx])
                    visit[xx]=1
                    dq.append(xx)
    return -1
n=int(input())
jump=list(map(int, input().split()))
visit=[0]*(n+1)
dp=[1001]*(n+1)
result=BFS(1)
print(result)

    