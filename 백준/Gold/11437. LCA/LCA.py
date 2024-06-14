import sys
input=sys.stdin.readline
sys.setrecursionlimit(int(1e5))

n=int(input())
tree=[[] for _ in range(n+1)]
for _ in range(n-1):
    a,b=map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
d=[0]*(n+1)
check=[0]*(n+1)
parent=[0]*(n+1)
def DFS(x, depth):
    check[x]=1
    d[x]=depth
    for next in tree[x]:
        if not check[next]:
            parent[next]=x
            DFS(next, depth+1)
def lca(x,y):
    while d[x]!=d[y]:
        if d[x]>d[y]:
            x=parent[x]
        else:
            y=parent[y]
    while x!=y:
        x=parent[x]
        y=parent[y]
    return x
DFS(1,0)
m=int(input())
for _ in range(m):
    a,b=map(int, input().split())
    print(lca(a,b))