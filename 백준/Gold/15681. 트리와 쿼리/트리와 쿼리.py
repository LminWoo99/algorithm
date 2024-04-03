import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**9)
def DFS(x):
    visit[x]=1
    for node in graph[x]:
        if not visit[node]:
            DFS(node)
            visit[x]+=visit[node]
            
                
n,r,q=map(int, input().split())
visit = [0] * (n+1)
graph=[[] for _ in range(n+1)]

for _ in range(n-1):
    x,y=map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
DFS(r)
for _ in range(q):
    x=int(input())
    print(visit[x])