import sys, heapq
input=sys.stdin.readline
def solution(start):
    hq=[]
    distance=[int(1e9)]*(n+1)
    heapq.heappush(hq, (0,start))
    distance[start]=0
    while hq:
        dist, cur_node=heapq.heappop(hq)
        if dist>distance[cur_node]:
            continue
        for next_node, next_dist in graph[cur_node]:
            if distance[next_node]>next_dist+dist:
                distance[next_node]=next_dist+dist
                heapq.heappush(hq, (next_dist+dist, next_node))
    return distance
T=int(input())
for _ in range(T):
    n,m,t=map(int, input().split())
    s, g, h=map(int, input().split())
    graph=[[] for _ in range(n+1)]
    for _ in range(m):
        a,b,d=map(int, input().split())
        graph[a].append((b,d))
        graph[b].append((a,d))
    destination=[]
    for _ in range(t):
        destination.append(int(input()))
    
    startDistance=solution(s)
    # 교차점중 거리가 큰게 기준이다. 최단거리를 구한것이고 거리가 큰게 g와 h사이에 도로로 지나갔다는 것
    if startDistance[g]<startDistance[h]:
        newS=h
    else:
        newS=g
    secondDistance=solution(newS)
    res=[]
    for dest in destination:
        # 교차점을 지났을때의 목적지 거리+출발지에서의 교차점 거리 == 출발지에서 목적지까지의 최단 거리같아야함
        if startDistance[newS]+secondDistance[dest]==startDistance[dest]:
            res.append(dest)
    res.sort()
    print(*res)