from collections import deque
def bfs(x,y):
    dq=deque()
    dq.append((x,y))
    while dq:
        x, y=dq.popleft()
        for i in range(4):
                xx=x+dx[i]
                yy=y+dy[i]
                if 0<=xx<n and 0<=yy<m and a[xx][yy]==1:
                    dq.append((xx,yy))
                    a[xx][yy]=a[x][y]+1    
n, m=map(int, input().split())
a=[list(map(int, input()))for _ in range(n)]
dx=[-1,0,1,0]
dy=[0,1,0,-1]
bfs(0,0)
print(a[n-1][m-1])