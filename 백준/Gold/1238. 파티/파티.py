import sys
input=sys.stdin.readline
import heapq
def solution(i):
    dist=[int(1e9)]*(n+1)
    dist[i]=0
    hq=[]
    heapq.heappush(hq, (0,i))
    while hq:
        t, start=heapq.heappop(hq)
        if dist[start]<t:
            continue
        for next, next_t in graph[start]:
            cost=next_t+t
            if dist[next]>cost:
                dist[next]=cost
                heapq.heappush(hq, (cost, next))
    return dist           



n,m,x=map(int , input().split())
graph=[[] for _ in range(n+1)]
for _ in range(m):
    a,b,t=map(int, input().split())
    graph[a].append((b,t))
res=[]
for i in range(1, n+1):
    if i!=x:
        tmp=solution(i)
        tmp2=solution(x)
        res.append(tmp[x]+tmp2[i])
print(max(res))

