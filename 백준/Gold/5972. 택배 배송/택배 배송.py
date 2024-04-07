import sys
import heapq
def solution(graph):
    start, weight=1, 0

    hq=[]
    distance[1]=0
    heapq.heappush(hq, (weight, start))
    while hq:
        weight, start=heapq.heappop(hq)
        if start==n:
            break
        if distance[start]<weight:
            continue
        for b,c in graph[start]:
            if distance[b]>weight+c:
                distance[b]=weight+c
                heapq.heappush(hq, (distance[b], b))
            
input=sys.stdin.readline
n,m =map(int, input().split())
graph=[[] for _ in range(n+1)]
distance=[int(1e9)]*(n+1)
for _ in range(m):
    a,b,c=map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
solution(graph)
print(distance[-1])