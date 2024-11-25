import sys
from collections import deque
input=sys.stdin.readline
dx=[-1,0,1,0]
dy=[0,1,0,-1]
def BFS(x,y):
    dq=deque()
    dq.append((x,y))
    visit[x][y]=1
    while dq:
        x,y=dq.popleft()
        for i in range(4):
            xx,yy=x+dx[i], y+dy[i]
            if 0<=xx<n and 0<=yy<m:
                if not visit[xx][yy] and board[xx][yy]==0:
                    visit[xx][yy]=1
                    dq.append((xx,yy))
                elif board[xx][yy]==1:
                    visit[xx][yy]+=1
n,m=map(int, input().split())

board=[list(map(int, input().split())) for _ in range(n)]

res=0
while True:
    visit=[[0]*m for _ in range(n)]
    BFS(0,0)
    res+=1
    for i in range(n):
        for j in range(m):
            if visit[i][j]>=2:
                board[i][j]=0
    flag=False
    for i in range(n):
        for j in range(m):
            if board[i][j]==1:
                flag=True
                break
        if flag:
            break
    if not flag:
        break
print(res)