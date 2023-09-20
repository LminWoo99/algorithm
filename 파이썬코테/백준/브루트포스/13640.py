import sys
from collections import deque
input=sys.stdin.readline
def BFS(nx,ny,nxx,nyy):
    global cnt
    dq=deque((nx,ny,nxx,nyy))
    visit=[]
    visit.append((nx,ny,nxx,nyy))
    count=0
    while dq:
        nx,ny,nxx, nyy=dq.popleft()
        if count>10:
            print(-1)
            return 
        for i in range(4):
            
            rx=nx+dx[i]
            ry=ny+dy[i]
            rxx=nxx+dx[i]
            ryy=nyy+dy[i]
            if not (0<rx<n and 0<ry<m) and not (0<rxx<n and 0<ryy<m):
                continue
            
            
            

n, m=map(int, input().split())
a=[]
dx=[-1,0,1,0]
dy=[0,1,0,-1]
x,y,xx,yy=0,0,0,0
cnt=0
for i in range(n):
    a.append(list(input().rstrip()))
    for j in range(m):
        if a[i][j]=='R':
            x,y=i,j
        elif  a[i][j]=='B':
            xx,yy=i,j
BFS(x,y,xx,yy)