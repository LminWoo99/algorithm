import sys
input=sys.stdin.readline
from collections import defaultdict,deque
t=int(input())
wow=[]

for _ in range(t):
    n,m=map(int, input().split())
    building=list(map(int, input().split()))
    res=[0]*(n+1)
    dq=deque()
    build_order=defaultdict(list)
    for _ in range(m):
        x,y=map(int, input().split())
        build_order[x].append(y)
        res[y]+=1
    win=int(input())
    cur=1
    dp = [0 for _ in range(n + 1)]
    for i in range(1, n+1):
        if res[i]==0:
            dq.append(i)
            dp[i] = building[i - 1]
    while dq:
        x=dq.popleft()
        for i in build_order[x]:
            res[i]-=1
            dp[i]=max(dp[i], dp[x]+building[i-1])
            if res[i]==0:
                dq.append(i)

    wow.append(dp[win])
for i in range(len(wow)):
    print(wow[i])
    

