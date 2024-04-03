import sys
import heapq
input=sys.stdin.readline
INF=int(1e9)
def solution(graph,d):
    g=len(graph)
    dist=[INF]*g
    hq=[]
    heapq.heappush(hq, (0,d))
    dist[d]=0
    while hq:
        dis, start=heapq.heappop(hq)
        if dist[start]<dis:
            continue
        for a in graph[start]:
            cost=dis+a[1]
            if cost<dist[a[0]]:
                dist[a[0]]=cost
                heapq.heappush(hq, (cost, a[0]))
    return dist
t=int(input())
for _ in range(t):
    n,d,c=map(int, input().split())
    graph=[[] for _ in range(n+1)]
    for i in range(d):
        a,b,s=map(int, input().split())
        graph[b].append((a,s))
    a=solution(graph,c)
    tmp=a.count(INF)
    dis=0
    for i in range(len(a)):
        if a[i]!=INF:
            dis=max(a[i],dis)
            
    print(n+1-tmp, dis)