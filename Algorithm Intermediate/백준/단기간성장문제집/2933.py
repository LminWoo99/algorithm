import sys
input=sys.stdin.readline
from collections import deque
def solution(index,L):
    x,y=r-index,0
    if L%2==1:
        for i in range(c):
            if cave[x][i]=='x':
                cave[x][i]='.'
                y=i
                break
    else:
        for i in range(c-1, -1,-1):
            if cave[x][i]=='x':
                cave[x][i]='.'
                y=i
                break
    for d in range(4):
        nx,ny=x+dx[d],y+dy[d]
        if 0<=nx<r and 0<=ny<c and cave[nx][ny]=='x':
            dq.append((nx,ny))
        
def BFS(x,y):
    q=deque()
    q.append((x,y))
    visit=[[0]*c for _ in range(r)]
    visit[x][y]=1
    fall_list=[]
    while q:
        x,y=q.popleft()
        if x==r-1:
            return
        if cave[x+1][y]=='.':
            fall_list.append((x,y))
        for i in range(4):
            xx=x+dx[i]
            yy=y+dy[i]
            if 0<=xx<r and 0<=yy<c and visit[xx][yy]==0 and cave[xx][yy]=='x':
                visit[xx][yy]=1
                q.append((xx,yy))
    fall(visit, fall_list)
    
def fall(visit, fall_list):
    dist, flag=1,0
    while True:
        for i,j in fall_list:
            if i+dist==r-1:
                flag=1
                break
            if cave[i+dist+1][j]=='x' and visit[i+dist+1][j]==0:
                flag=1
                break
        if flag:
            break
        dist+=1
        
    for i in range(r-2, -1, -1):
        for j in range(c):
            if cave[i][j]=='x' and visit[i][j]:
                cave[i][j]='.'
                cave[i+dist][j]='x'
                
r,c=map(int, input().split())
cave=[list(input().rstrip()) for _ in range(r)]
n=int(input())
height=list(map(int,input().split()))
dx=[-1,0,1,0]
dy=[0,1,0,-1]
check=[]
dq=deque()
tmp=1
while n:
    index=height.pop(0)
    solution(index, tmp)
    while dq:
        x,y=dq.popleft()
        BFS(x,y)
    tmp +=1
    n-=1
for i in range(r):
    for j in range(c):
        print(cave[i][j],end='')
    print()