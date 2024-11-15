import sys
import heapq
input=sys.stdin.readline
def dijkstra(start):
    hq=[]
    distance[start]=0
    heapq.heappush(hq, (0, start))
    while hq:
        dist, cur_node= heapq.heappop(hq)
        if distance[cur_node]<dist:
            continue
        for next_node, next_dist in graph[cur_node]:
            if distance[next_node]>dist+next_dist:
                # if next_node==n:
                #     check[cur_node]=1
                distance[next_node]=dist+next_dist
                heapq.heappush(hq, (dist+next_dist, next_node))
    
n,e=map(int, input().split())
graph=[[]*(n+1) for _ in range(n+1)]
for _ in range(e):
    a,b,c=map(int, input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])

v=list(map(int, input().split()))
check=[0]*(n+1)
start=1
tmp1=0
tmp2=0
for i in range(2):
    distance=[int(1e9)]*(n+1)
    dijkstra(start)
    tmp1+=distance[v[i]]
    start=v[i]
distance=[int(1e9)]*(n+1)
dijkstra(start)
tmp1+=distance[n]
start=1
for i in range(1,-1,-1):
    distance=[int(1e9)]*(n+1)
    dijkstra(start)
    tmp2+=distance[v[i]]
    start=v[i]
distance=[int(1e9)]*(n+1)
dijkstra(start)
tmp2+=distance[n]
if tmp1>=int(1e9) and tmp2>=int(1e9):
    print(-1)
else:
    print(min(tmp1, tmp2))