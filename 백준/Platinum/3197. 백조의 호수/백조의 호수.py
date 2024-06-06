import sys
input=sys.stdin.readline
from collections import deque
dx=[-1,0,1,0]
dy=[0,1,0,-1]
def check_swan(dq):
    next_dq=deque()
    while dq:
        x,y=dq.popleft()
        if x==x2 and y==y2:
            return 1, None
        for i in range(4):
            xx,yy=x+dx[i], y+dy[i]
            if 0<=xx<r and 0<=yy<c and not visit[xx][yy] and lake[xx][yy]!='X':
                visit[xx][yy]=1
                dq.append((xx,yy))     
            elif 0<=xx<r and 0<=yy<c and not visit[xx][yy] and lake[xx][yy]=='X':
                visit[xx][yy]=1
                next_dq.append((xx,yy))
    return False, next_dq
def BFS(water):
    next_water=deque()
    while water:
        x,y=water.popleft()
        for i in range(4):
            xx,yy=x+dx[i], y+dy[i]
            if 0<=xx<r and 0<=yy<c and lake[xx][yy]=='X':
                lake[xx][yy]='.'
                next_water.append((xx,yy))
    return next_water
r,c=map(int, input().split())
lake=[list(input().rstrip()) for _ in range(r)]
swan=[]
water=deque()
for i in range(r):
    for j in range(c):
       if lake[i][j]=='L':
           swan.append((i,j))
           water.append((i,j))
       elif lake[i][j]=='.':
           water.append((i,j))

x1,y1=swan[0][0], swan[0][1]           
x2,y2=swan[1][0], swan[1][1]
visit=[[0]*c for _ in range(r)]
res=0

dq=deque()
visit[x1][y1]=1
dq.append((x1,y1))

while True:
    found, dq=check_swan(dq)
    if found:
        break
    res+=1
    water=BFS(water)
print(res)