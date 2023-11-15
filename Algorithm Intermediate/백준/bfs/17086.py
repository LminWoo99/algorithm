import sys
input=sys.stdin.readline

from collections import deque
def BFS():
    while dq:
        x,y=dq.popleft()
        for i in range(8):
            xx=x+dx[i]
            yy=y+dy[i]
            if 0<=xx<n and 0<=yy<m and not a[xx][yy]:
                a[xx][yy]=a[x][y]+1
                dq.append((xx,yy))

n,m =map(int, input().split())
a=[list(map(int, input().split())) for _ in range(n)]

dx=[-1,0,1,0,-1,-1,1,1]
dy=[0,1,0,-1,-1,1,-1,1]
tmp=0
dq=deque()
for i in range(n):
    for j in range(m):
        if a[i][j]==1:
            dq.append((i,j))
BFS()
print(max(map(max, a))-1)

