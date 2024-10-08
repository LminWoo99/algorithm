import sys, heapq
input=sys.stdin.readline
INF=int(1e9)
def dijkstra(start):

    visit[start]=0
    hq=[]
    heapq.heappush(hq, (0, start))
    while hq:
        distance, x=heapq.heappop(hq)
        if visit[x]<distance:
            continue
        for next_node , next_distance in graph[x]:
            tmp=next_distance+distance
            if visit[next_node]>tmp:
                visit[next_node]=tmp
                heapq.heappush(hq, (tmp, next_node))
        
        
V,E=map(int, input().split())
k=int(input())
graph=[[]*(V+1) for _ in range(V+1)]
for _ in range(E):
    u,v,w=map(int, input().split())
    graph[u].append((v,w))

visit=[INF]*(V+1)
dijkstra(k)
for i in range(1, V+1):
    if visit[i]!=INF:
        print(visit[i])
    else:
        print("INF")