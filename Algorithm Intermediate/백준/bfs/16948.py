import sys
input=sys.stdin.readline
from collections import deque

def BFS(r, c):
    dq=deque()
    dq.append([r,c])
    cnt=0
    while dq:
        x, y=dq.popleft()
        if x==rex and y==rey:
            break
        for i in range(6):
            xx=dx[i]+x
            yy=dy[i]+y        
            if 0<=xx<n and 0<=yy<n and visit[xx][yy]==False:
                visit[xx][yy]=True
                check[xx][yy]=check[x][y]+1
                dq.append([xx,yy])
dx=[-2,-2,0,0,2,2]
dy=[-1,1,-2,2,-1,1]
    
n=int(input())
a=list(map(int , input().split()))
visit=[[False]*n for _ in range(n)]
check=[[0]*n for _ in range(n)]
r, c=a[0], a[1]
visit[r][c]=True
rex, rey=a[2], a[3]
BFS(r,c)
if check[rex][rey]==0:
    print(-1)
else:
    print(check[rex][rey])