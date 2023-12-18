import sys
input=sys.stdin.readline
from collections import deque
n=int(input())
k=int(input())
board=[[0]*n for _ in range(n)]
for i in range(k):
    a,b=map(int, input().split())
    board[a-1][b-1]=1
L=int(input())
rotate=[]
res=0
dx=[-1,0,1,0]
dy=[0,1,0,-1]
d=1
for i in range(L):
    x,c=input().rstrip().split()
    rotate.append((x,c))
snake=deque()
snake.append((0,0))
while True:
    
    if len(rotate)!=0 and int(rotate[0][0])==res:
        if rotate[0][1]=='L':
            d=(d+3)%4
        else:
            d=(d+1)%4
        rotate.pop(0)
    res+=1
    x,y=snake[0][0], snake[0][1]
    xx, yy=x+dx[d], y+dy[d]
    if xx<0 or yy<0 or xx>=n or yy>=n or (xx,yy) in snake:
        print(res)
        sys.exit()
    elif 0<=xx<n and 0<=yy<n and board[xx][yy]==1 :
        board[xx][yy]=0
        snake.appendleft((xx,yy))
    elif 0<=xx<n and 0<=yy<n and board[xx][yy]==0 :
        snake.appendleft((xx,yy))
        snake.pop()
    
    
