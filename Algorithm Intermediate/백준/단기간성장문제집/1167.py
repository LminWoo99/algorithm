import sys
input=sys.stdin.readline
# 트리의 지름 성질 이해하기!
# 임의의 점에서 가장 먼 정점을 구하고 그 정점의 가장 먼 정점의 길이가 트리의 지름이다
#  늘어진 추로 생각
sys.setrecursionlimit(10**9)
def DFS(x, len_tree):
    for v,d in graph[x]:
        if visit[v]==-1:
            visit[v]=len_tree+d
            DFS(v, visit[v])
n=int(input())
graph=[[] for _ in range(n+1)]
for _ in range(n):
    tmp=list(map(int, input().split()))
    cnt=tmp[0]
    idx=1
    while tmp[idx]!=-1:
        x,y=tmp[idx], tmp[idx+1]
        graph[cnt].append((x,y))
        idx+=2            

visit=[-1]*(n+1)
visit[1]=0
DFS(1,0)
tmp=[0,0]
for i in range(1, len(visit)):
    if visit[i]> tmp[1]:
        tmp[1]=visit[i]
        tmp[0]=i
visit=[-1]*(n+1)
visit[tmp[0]]=0
DFS(tmp[0], 0)
print(max(visit))
        
        
        
