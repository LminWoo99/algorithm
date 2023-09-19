import sys
sys.setrecursionlimit(1000000)
def dfs(v):
    for i in graph[v]:
        if visit[i]==0:
            visit[i]=v
            dfs(i)

n=int(input())
graph=[[] for _ in range(n+1)]
for i in range(n-1):
    a,b=map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
visit=[0]*(n+1)
dfs(1)
for x in range(2,n+1):
    print(visit[x])