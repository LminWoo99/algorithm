import heapq
def solution(n, s, a, b, fares):
    graph=[[] for _ in range(n+1)]
    for c,d,f in fares:
        graph[c].append((d,f))
        graph[d].append((c,f))
    
    def solve(start):
        hq=[]
        heapq.heappush(hq, (0,start))
        distance=[int(1e9)]*(n+1)
        distance[start]=0
        while hq:
            dist, start=heapq.heappop(hq)
            if distance[start]<dist:
                continue
                
            for next in graph[start]:
                next_cost=next[1]+dist
                if distance[next[0]]>next_cost:
                    distance[next[0]]=next_cost
                    heapq.heappush(hq, (next_cost, next[0]))
        return distance
    D = [0] + [solve(i) for i in range(1, n+1)] 
    path = int(1e9)
    for i in range(1, n+1):
        path = min(path, D[s][i] + D[i][a] + D[i][b])
    
    return path