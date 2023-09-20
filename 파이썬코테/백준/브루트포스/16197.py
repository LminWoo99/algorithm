import sys
input=sys.stdin.readline
from collections import deque

def BFS(x,y,xx,yy):
    check=[[[[-1]*m for _ in range(n)] for _ in range(m)]for _ in range(n)]
    check[x][y][xx][yy]=0
    dq=deque([(x,y,xx,yy)])
    while dq:
        x,y,xx,yy=dq.popleft()
        if check[x][y][xx][yy] >=10:
            break
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            nxx=xx+dx[i]
            nyy=yy+dy[i]
            if not(0<=nx <n and 0<= ny <m) and not(0<=nxx <n and 0<= nyy <m):
                continue
            if not(0<=nx <n and 0<= ny <m):
                return check[x][y][xx][yy]+1
            if not(0<=nxx <n and 0<= nyy <m):
                return check[x][y][xx][yy]+1
            if a[nx][ny] =='#':
                nx-=dx[i]
                ny-=dy[i]
            if a[nxx][nyy] =='#':
                nxx-=dx[i]
                nyy-=dy[i]
            if check[nx][ny][nxx][nyy] == -1:
                check[nx][ny][nxx][nyy]= check[x][y][xx][yy]+1
                dq.append([nx, ny , nxx ,nyy])
    return -1
n,m=map(int, input().split())


cnt=0
dx=[-1,0,1,0]
dy=[0,1,0,-1]    

x,y,xx,yy=0,0,0,0
a=[]
flag=True
for i in range(n):
    a.append(list(input().rstrip()))
    for j in range(m):
        if a[i][j]=='o':
            if flag:
                x,y=i,j            
                flag=False
            else:
                xx,yy=i,j
print(BFS(x,y,xx,yy))