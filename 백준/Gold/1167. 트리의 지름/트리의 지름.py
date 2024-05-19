import sys
input=sys.stdin.readline
def DFS(x, cnt):
    for next_node, next_distance in tree[x]:
        dist=next_distance+cnt
        if visit[next_node]==-1:
            visit[next_node]=dist
            DFS(next_node, dist)
    return 

v=int(input())
tree=[[] for _ in range(v+1)]
visit=[-1]*(v+1)
for i in range(v):
    tmp=list(map(int, input().split()))
    cnt=tmp[0]
    idx=1
    while tmp[idx]!=-1:
        tree[cnt].append((tmp[idx], tmp[idx+1]))
        idx+=2
tmp=[0,0]
visit[1]=0
DFS(1, 0)
for i in range(1, v+1):
    if tmp[1]<visit[i]:
        tmp[1]=visit[i]
        tmp[0]=i
visit=[-1]*(v+1)
visit[tmp[0]]=0
DFS(tmp[0], 0)


print(max(visit))