import heapq
answer = 0
def solution(n, costs):
    graph=[[]*(n) for _ in range(n)]
    for start, end, cost in costs:
        graph[start].append((end,cost))
        graph[end].append((start,cost))
    visit=[0]*n
    def dijkstra(cost, start):
        global answer
        hq=[]
        heapq.heappush(hq, (cost, start))
        while hq:
            cnt, start=heapq.heappop(hq)
            if visit[start]:
                continue
            visit[start]=1
            answer+=cnt
            for a,b in graph[start]:
                if not visit[a]:
                    heapq.heappush(hq, (b, a))
    dijkstra(0,0)
    return answer