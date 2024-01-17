import sys
input=sys.stdin.readline
import heapq
def solution(start):
    dist=[INF for _ in range(n+1)]
    dist[start]=0
    hq=[]
    heapq.heappush(hq, [0,start])
    while hq:
        distance, node= heapq.heappop(hq)
        if dist[node]<distance:
            continue
        for next_node, weight in graph[node]:
            if dist[next_node]>weight+distance:
                dist[next_node]=weight+distance
                path[next_node]=node
                visit[next_node]=visit[node]+1
                heapq.heappush(hq, [dist[next_node], next_node])
    return dist
                
n=int(input())
m=int(input())
INF=int(1e9)
path=[0]*(n+1)
visit=[1]*(n+1)
graph=[[] for _ in range(n+1)]
for _ in range(m):
    x,y,z=map(int, input().split())
    graph[x].append((y,z))
start,end=map(int, input().split())
res=solution(start)
print(res[end])
print(visit[end])
result=[]
result.append(end)
tmp=path[end]
for i in range(visit[end]-1):
    result.append(tmp)
    tmp=path[tmp]
print(*result[::-1])