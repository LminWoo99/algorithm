import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**7)
def DFS(x,y):
    for next_node, weight in tree[x]:
        if visit[next_node]==-1:
            visit[next_node]=weight+y
            DFS(next_node,visit[next_node])
    
n=int(input())
tree=[[]*(n+1) for _ in range(n+1)]
for _ in range(n-1):
    x,y,weight=map(int, input().split())
    tree[x].append(([y,weight]))
    tree[y].append(([x,weight]))
visit=[-1]*(n+1)
visit[1]=0
DFS(1,0)
tmp=[0,0]
for i in range(1, n+1):
    if tmp[0]<visit[i]:
        tmp[0]=visit[i]
        tmp[1]=i
visit=[-1]*(n+1)
visit[tmp[1]]=tmp[0]
DFS(tmp[1],0)
print(max(visit))