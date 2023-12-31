import sys
import collections
from collections import deque
input=sys.stdin.readline

n,m = map(int, input().split())
graph=collections.defaultdict(list)
dq=deque()
res=[0 for i in range(n+1)]
cur=[0 for i in range(n+1)]
for _ in range(m):
    x,y=map(int, input().split())
    graph[x].append(y)
    res[y]+=1
    
for i in range(1, n+1):
    if res[i]==0:
        dq.append((i,1))
        cur[i]=1
while dq:
    a, cnt=dq.popleft()
    for i in graph[a]:
        res[i]-=1
        if res[i]==0:
            dq.append((i, cnt+1))
            cur[i]=cnt+1
print(*cur[1:])

    
    