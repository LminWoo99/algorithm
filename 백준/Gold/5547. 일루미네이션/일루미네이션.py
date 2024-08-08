import sys
from collections import deque
input=sys.stdin.readline
def BFS(x,y):
    global res
    dq=deque()
    dq.append((x,y))
    visit[x][y]=1
    while dq:
        x,y=dq.popleft()
        for i in range(6):
            if x%2==0:
                xx,yy=x+even[i][0], y+even[i][1]
            else:
                xx,yy=x+odd[i][0], y+odd[i][1]
            if 0<=xx<h+2 and 0<=yy<w+2:
                if board[xx][yy]==0 and not visit[xx][yy]:
                    dq.append((xx,yy))
                    visit[xx][yy]=1
                elif board[xx][yy]==1:
                    res+=1
    return res
odd=[[-1,0],[0,-1],[1,0],[1,1], [0,1], [-1,1]]
even=[[-1,-1],[0,-1], [1,-1],[1,0], [0,1],[-1,0]]
w,h=map(int, input().split())
board = [[0 for _ in range(w+2)] for _ in range(h+2)]
for i in range(1, h+1):
    board[i][1:w+1] = map(int, input().split())
res=0
visit=[[0]*(w+2) for _ in range(h+2)]
print(BFS(0,0))
