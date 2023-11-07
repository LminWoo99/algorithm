import sys
from collections import deque
def BFS(mid):
    visit[start]=1
    dq=deque()
    dq.append(start)
    while dq:
        now= dq.popleft()
        if now == end:
            return True
        for nx, ny in island[now]:
            if visit[nx]==0 and ny>=mid:
                dq.append(nx)
                visit[nx]=1
            
n,m =map(int, input().split())
island=[[] for _ in range(n+1)]
for i in range(m):
    a,b,c=map(int, input().split())
    island[a].append((b,c))
    island[b].append((a,c))
for i in range(1, n+1):
    island[i].sort(reverse=True)

start, end = map(int, input().split())
low, high = 1, 1000000000
while low <= high:
        visit = [0 for _ in range(n + 1)]
        mid = (low + high) // 2
        if BFS(mid): 
            low = mid + 1
        else: 
            high = mid - 1

print(high)