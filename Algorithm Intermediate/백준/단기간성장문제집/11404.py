import sys
input=sys.stdin.readline
def Floyd_Warshall():
    dist=[[INF]*(n+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for dest, cost in graph[i]:
            dist[i][dest]=min(dist[i][dest], cost)
    
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if i!=j and dist[i][j]>dist[i][k]+dist[k][j]:
                    dist[i][j]=dist[i][k]+dist[k][j]
    return dist
                
n=int(input())
m=int(input())
INF=int(1e9)
graph=[[] for _ in range(n+1)]
for _ in range(m):
    a,b,c=map(int, input().split())
    graph[a].append((b,c))
dist=Floyd_Warshall()
for i in range(1, n+1):
    for j in range(1, n+1):
        if dist[i][j]==INF:
            print(0, end=' ')
        else:
            print(dist[i][j], end=' ')
    print()