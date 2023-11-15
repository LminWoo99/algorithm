import sys
input=sys.stdin.readline
from collections import deque

def BFS(x,y,cnt):
    dq=deque()
    dq.append((x,y,cnt))
    global visit
    res=0
    while dq:
        x,y,cnt=dq.popleft()
        if x==h-1 and y==w-1:
            return visit[h-1][w-1][cnt]
        else:
            for i in range(4):
                xx=x+dx[i]
                yy=y+dy[i]
                if 0<=xx<h and 0<=yy<w and visit[xx][yy][cnt]==0 and a[xx][yy]!=1:
                    visit[xx][yy][cnt]=visit[x][y][cnt]+1
                    dq.append((xx,yy, cnt))
                            
            if cnt<k:                   
                for i in range(8):
                    xx=x+horseX[i]
                    yy=y+horseY[i]
                    if 0<=xx<h and 0<=yy<w and visit[xx][yy][cnt+1]==0 and a[xx][yy]!=1:
                        visit[xx][yy][cnt+1]=visit[x][y][cnt]+1
                        dq.append((xx,yy, cnt+1))
    return -1


k=int(input())
w,h=map(int, input().split())
a=[list(map(int, input().split())) for _ in range(h)]

dx=[-1,0,1,0]
dy=[0,1,0,-1]
horseX=[2,2, 1, -1, -2,-2, 1, -1]
horseY=[1, -1, 2, 2,  1, -1, -2, -2]

visit=[[[0]*(k+1) for _ in range(w)] for _ in range(h)]
print(BFS(0,0,0))