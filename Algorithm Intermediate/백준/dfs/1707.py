import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)
def DFS(start, visit, graph, group):
    visit[start]=group
    for i in graph[start]:
        if visit[i]==0:
            result=DFS(i, visit, graph, -group)
            if not result:
                return False
        else:
            if visit[i]== group:
                return False
    return True
t=int(input())
for i in range(t):
    v,e=map(int, input().split())
    graph=[[] for _ in range(v+1)]
    visit=[0]*(v+1)
    for j in range(e):
        a,b=map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    for k in range(1, v+1):
        if visit[k]==0:
            result=DFS(k, visit, graph, 1)
            if not result:
                break
    if result:
        print("YES")
    else:
        print("NO")