import sys
sys.setrecursionlimit(1000000)
def dfs(x,y):
    global res
    if x==m-1 and y==n-1:
        return 1
    if visit[x][y]==-1:
        visit[x][y]=0
        for i in range(4):
            xx=x+dx[i]
            yy=y+dy[i]
            if 0<=xx<m and 0<=yy<n and a[xx][yy]<a[x][y]:
                visit[x][y]+=dfs(xx,yy)
    return visit[x][y]
m,n=map(int, input().split())
a=[list(map(int, input().split())) for _ in range(m)]
dx=[-1,0,1,0]
dy=[0, 1, 0, -1]
visit=[[-1]*n for _ in range(m)]
res=0

print(dfs(0,0))