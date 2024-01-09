import sys
input = sys.stdin.readline
# 다익스트라
from heapq import heappop, heappush
def solution(start):
    dist=[INF for _ in range(n+1)]
    dist[start]=0
    heap=[]
    # 첫번째요소르 기준으로 정렬
    heappush(heap, [0, start])
    while heap:
        weight, node= heappop(heap)
        # 힙임으로 가장 처음값이 가장 작으므로 시간 단축
        if dist[node] < weight:
            continue
        for next, cost in graph[node]:
            if dist[next]>weight+cost:
                dist[next]=weight+cost
                heappush(heap, [dist[next], next])
    return dist
T=int(input())
INF=int(1e9)
for _ in range(T):
    n,m,t=map(int, input().split())
    s,g,h=map(int, input().split())
    graph=[[] for _ in range(n+1)]
    for i in range(m):
        a,b,d=map(int, input().split())
        graph[a].append((b,d))
        graph[b].append((a,d))
    dest=[]
    for i in range(t):
        x=int(input())
        dest.append(x)
    distFromS=solution(s)
    if distFromS[g]>distFromS[h]:
        newStart=g
    elif distFromS[g]<distFromS[h]:
        newStart=h
    distFromNewS=solution(newStart)
    res=[]
    for i in dest:
        if distFromS[newStart]+distFromNewS[i]==distFromS[i]:
            res.append(i)
    res.sort()
    print(*res)