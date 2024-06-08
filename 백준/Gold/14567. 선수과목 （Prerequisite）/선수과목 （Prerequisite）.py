import sys
input=sys.stdin.readline
from collections import deque
n,m=map(int, input().split())
degree=[0]*(n+1)
graph=[[]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a,b=map(int, input().split())
    graph[a].append(b)
    degree[b]+=1
dq=deque()
res=[0]*n
for i in range(1, n+1):
    if degree[i]==0:
        dq.append((i,1))        
while dq:
    start,cur=dq.popleft()
    res[start-1]=cur
    for next in graph[start]:
        degree[next]-=1
        if degree[next]==0:
            dq.append((next, cur+1))
print(*res)