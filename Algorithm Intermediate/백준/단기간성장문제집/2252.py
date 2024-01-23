import sys
input=sys.stdin.readline
from collections import deque
# 위상정렬
n , m=map(int, input().split())
graph=[[] for _ in range(n+1)]
visit=[0 for _ in range(n+1)]
dq=deque()
for _ in range(m):
    a,b=map(int, input().split())
    graph[a].append(b)
    visit[b]+=1

res=[]
for i in range(1, n+1):
    if visit[i]==0:
        dq.append(i)
while dq:
    x=dq.popleft()
    res.append(x)
    for i in graph[x]:
        visit[i]-=1
        if visit[i]==0:
            dq.append(i)
                     
print(*res)