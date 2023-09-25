import sys
input=sys.stdin.readline
from collections import deque
def BFS(x,y,z):
    dq=deque()
    dq.append((x,y,z))
    while dq:
        x,y,c=dq.popleft()
        if x == n-1 and y == m-1:
            return visit[x][y][c]
        for i in range(4):
            xx=x+dx[i]
            yy=y+dy[i]
            if xx<0 or xx>=n or yy < 0 or yy>=m:
                continue
            if a[xx][yy] == 1 and c == 0:
                visit[xx][yy][1] = visit[x][y][0]+1
                dq.append((xx,yy,1))
            elif a[xx][yy]==0 and visit[xx][yy][c]==0:
                visit[xx][yy][c]= visit[x][y][c]+1
                dq.append((xx,yy,c))
    return -1
                            
n,m=map(int, input().split())
a=[list(map(int, input().rstrip())) for _ in range(n)]

visit=[[[0]*2 for _ in range(m)] for _ in range(n)]
visit[0][0][0]=1




dx=[-1,0,1,0]
dy=[0,1,0,-1]

print(BFS(0,0,0))
