import sys
input=sys.stdin.readline
from collections import deque
n,m=map(int, input().split())
singers=[]
dx=[0]*(n+1)
graph=[[]*(n+1) for _ in range(n+1)]
dq=deque()

for _ in range(m):
    tmp=list(map(int, input().split()))
    tmp.pop(0)
    singers.extend(tmp)
    for i in range(1, len(tmp)):
        dx[tmp[i]]+=1
        graph[tmp[i-1]].append(tmp[i])
for i in range(1, n+1):
    if dx[i]==0:
        dq.append(i)
res=[]
while dq:
    cur_singer=dq.popleft()
    res.append(cur_singer)
    for next_singer in graph[cur_singer]:
        dx[next_singer]-=1
        if dx[next_singer]==0:
            dq.append(next_singer)
if len(res)!=n:
    print(0)
else:
    for singer in res:
        print(singer)