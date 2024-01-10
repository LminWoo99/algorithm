import sys
input = sys.stdin.readline
INF = int(1e9)
for _ in range(int(input())):
    N, M, K = map(int, input().split())
    info = [[] for _ in range(N+1)]
    dist = [[INF]*(M+1) for _ in range(N+1)]
    dist[1][0] = 0 
    
    for _ in range(K):
        u, v, c, d = map(int, input().split())
        info[u].append((v, c, d))

    for cost in range(M+1):
        for city in range(1, N+1):
            if dist[city][cost] != INF:
                for dest, c, d in info[city]:
                    total_time = dist[city][cost] + d
                    total_cost = cost + c
                    
                    if total_cost <= M and total_time < dist[dest][total_cost]:
                        dist[dest][total_cost] = total_time
    res = min(dist[N])
    
    if res == INF:
        print("Poor KCM")
    else:
        print(res)