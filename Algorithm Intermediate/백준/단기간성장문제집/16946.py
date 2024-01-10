import sys
input=sys.stdin.readline
from collections import deque
def BFS(x,y):
    cnt=1
    dq=deque()
    dq.append((x,y))
    while dq:
        x,y=dq.popleft()
        zeros[x][y]=group
        for i in range(4):
            xx,yy=x+dx[i],y+dy[i]
            if 0<=xx<n and 0<=yy<m and visit[xx][yy]==0 and board[xx][yy]==0:
                cnt+=1
                visit[xx][yy]=1
                dq.append((xx,yy))
    return cnt
n , m=map(int, input().split())
board=[list(map(int, input().rstrip())) for _ in range(n)]
visit=[[0]*m for _ in range(n)]
info = {}
info[0] = 0
group=1
zeros = [[0] * m for _ in range(n)]

dx=[-1,0,1,0]
dy=[0,1,0,-1]
for i in range(n):
    for j in range(m):
        if board[i][j]==0 and visit[i][j]==0:
            visit[i][j]=1
            cnt=BFS(i,j)
            info[group]=cnt
            group+=1
for i in range(n):
    for j in range(m):
        tmpList=set()
        if board[i][j]:
            for dist in range(4):
                xx,yy=i+dx[dist], j+dy[dist]
                if 0<=xx<n and 0<=yy<m:
                    tmpList.add(zeros[xx][yy])
            for add in tmpList:
                board[i][j]+=info[add]
            board[i][j] %=10
for res in board:
    print("".join(map(str, res)))
