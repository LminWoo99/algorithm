import sys
from collections import deque
input=sys.stdin.readline
def BFS(start):
    dq=deque()
    dq.append(start)    
    visit[start]=1
    while dq:
        node=dq.popleft()
        for next_node in graph[node]:
            if visit[next_node]==-1:
                visit[next_node]=visit[node]^1
                dq.append(next_node)
            elif visit[node]==visit[next_node]:
                return False
    return True
                
    
n,m=map(int, input().split())
visit=[-1]*(n+1)
graph=[[] for _ in range(n+1)]
for _ in range(m):
    u,v=map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
answer=0
for i in range(1, n+1):
    if visit[i]==-1:
        flag=BFS(i)
        if not flag:
           break
if flag:
    lion=0
    rabbit=0
    for i in range(1, n+1):
        if visit[i]==1:
            lion+=1
        else:
            rabbit+=1
    answer=lion*rabbit*2
print(answer) 
