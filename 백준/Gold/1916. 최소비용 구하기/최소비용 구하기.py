import sys
input=sys.stdin.readline
import sys, heapq
input=sys.stdin.readline
def dijkstra(start, end):
    hq=[]
    distance[start]=0
    heapq.heappush(hq, (0, start))
    while hq:
        cost,node=heapq.heappop(hq)
        if node==end:
            break
        if distance[node]<cost:
            continue
        for next_cost, next_node in graph[node]:
            if distance[next_node]>next_cost+cost:
                distance[next_node]=next_cost+cost
                heapq.heappush(hq, (distance[next_node] ,next_node))
            
n=int(input()) #도시 갯수
m=int(input()) #버스 갯수
distance=[int(1e9)]*(n+1)
graph=[[]*(n+1) for _ in range(n+1)]

for _ in range(m):
    x,y , cost=map(int, input().split())
    graph[x].append((cost, y))
start, end = map(int, input().split())
dijkstra(start,end)
print(distance[end])