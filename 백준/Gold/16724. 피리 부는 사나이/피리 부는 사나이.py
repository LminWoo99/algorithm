import sys
input=sys.stdin.readline
from collections import defaultdict

info=defaultdict(list)
info['U']=[-1,0]
info['D']=[1,0]
info['L']=[0,-1]
info['R']=[0,1]
res=0
def DFS(x,y):
    global res
    visit[x][y]=1
    cycle.append([x,y])
    x,y=x+info[a[x][y]][0], y+info[a[x][y]][1]
    if visit[x][y]:
        if [x,y] in cycle:
            res+=1
    else:
        DFS(x,y)
n,m=map(int, input().split())
a=[list(input().rstrip()) for _ in range(n)]

visit=[[0]*m for _ in range(n)]


for i in range(n):
    for j in range(m):
        if not visit[i][j]:
            cycle=[]
            DFS(i,j)
print(res)