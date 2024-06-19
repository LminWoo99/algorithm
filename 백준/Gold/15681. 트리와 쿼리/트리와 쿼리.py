import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**9)
def DFS(node):
    visit[node]=1
    for next_node in trees[node]:
        if not visit[next_node]:
            DFS(next_node)
            visit[node]+=visit[next_node]
n,r,q=map(int, input().split())
trees=[[] for _ in range(n+1)]

for i in range(n-1):
    x,y=map(int, input().split())
    trees[x].append(y)
    trees[y].append(x)
visit=[0]*(n+1)
DFS(r)
for i in range(q):
    u=int(input())
    print(visit[u])