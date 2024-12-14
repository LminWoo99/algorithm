
import sys
input=sys.stdin.readline
from collections import deque
dx=[-1,0,1,0]
dy=[0,1,0,-1]
def BFS(x,y,cnt):
    dq=deque()
    dq.append((x,y))
    visit[x][y]=cnt
    while dq:
        x,y=dq.popleft()
        for i in range(4):
            xx ,yy = x+dx[i] , y+dy[i]
            if 0<=xx<n and 0<=yy<n and not visit[xx][yy] and islands[xx][yy]==1:
                visit[xx][yy]=cnt
                dq.append((xx,yy))
            elif 0<=xx<n and 0<=yy<n and not visit[xx][yy] and islands[xx][yy]==0:
                outside.append([xx,yy, cnt])
def check(x,y,cur):
    global res
    dq=deque()
    dq.append((x,y,0))
    visited=[[0]*n for _ in range(n)]
    while dq:
        x,y,cnt=dq.popleft()
        if visit[x][y]!=cur and islands[x][y]!=0:
            res=min(res, cnt)
            break
        for i in range(4):
            xx ,yy = x+dx[i] , y+dy[i]
            if 0<=xx<n and 0<=yy<n and not visited[xx][yy]:
                if islands[xx][yy]!=cur:
                    visited[xx][yy]=1
                    dq.append((xx,yy,cnt+1))
            
n=int(input())
islands=[list(map(int, input().split())) for _ in range(n)]


visit=[[0]*n for _ in range(n)]
## 일단 섬 이어 놓고 tmp로 채운다

tmp=1
outside=deque()
for i in range(n):
    for j in range(n):
        if not visit[i][j] and islands[i][j]==1:

            BFS(i,j, tmp)
            tmp+=1
res=int(1e9)
for x,y,cur in outside:
    check(x,y,cur)
print(res)