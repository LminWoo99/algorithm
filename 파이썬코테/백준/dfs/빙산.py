import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**5)
def dfs(x,y):
    for i in range(4):
        xx=dx[i]+x
        yy=dy[i]+y
        if 0<=xx<n and 0<=yy<m and visit[xx][yy]:
            visit[xx][yy]=False
            if a[xx][yy]!=0:
                dfs(xx,yy)
dx=[-1, 0, 1, 0]
dy=[0, 1, 0 , -1]

n,m=map(int, input().split())
a=[list(map(int, input().split())) for _ in range(n)]
visit=[[False]*m for _ in range(n)]
tmp=0
while True:
    tmp+=1
    for i in range(n):
        for j in range(m):
            if a[i][j]!=0:
                visit[i][j]=True
                c=a[i][j]
                for k in range(4):
                    nx=i+dx[k]
                    ny=j+dy[k]
                    if 0<=nx<n and 0<=ny<m and not visit[nx][ny]:
                        if a[nx][ny]==0:
                            c-=1
                            if c==0:
                                break
                a[i][j]=c
    ch=0
    for i in range(n):
        for j in range(m):
            if a[i][j]!=0 and visit[i][j]:
                dfs(i,j)
                ch+=1
            elif a[i][j]==0 and visit[i][j]:
                visit[i][j]=False
    if ch>=2:
        print(tmp)
        break
    elif ch==0:
        print(0)
        break