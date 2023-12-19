import sys
input=sys.stdin.readline
from itertools import combinations
from collections import deque
import copy
def BFS():
    global board_tmp
    res=0
    dq=deque(birus)
    visit[dq[0][0]][dq[0][1]]=1
    while dq:
        x,y=dq.popleft()
        for i in range(4):
            xx, yy=x+dx[i], y+dy[i]
            if 0<=xx<n and 0<=yy<m and visit[xx][yy]==0:
                if board_tmp[xx][yy]==0:
                    visit[xx][yy]=1
                    dq.append((xx,yy))
                    board_tmp[xx][yy]=2

    for i in range(n):
        for j in range(m):
            if board_tmp[i][j]==0:
                res+=1
    return res
n,m=map(int, input().split())

board=[list(map(int, input().split())) for _ in range(n)]
dx=[-1,0,1,0]
dy=[0,1,0,-1]
empty=[]
birus=[]
cnt=0
cnt_one=0
result=0
for i in range(n):
    for j in range(m):
        if board[i][j]==2:
            birus.append((i,j))
        elif board[i][j]==0:
            cnt+=1
            empty.append((i,j))
        else:
            cnt_one+=1

for i in combinations(empty, 3):
    board_tmp=copy.deepcopy(board)
    for j in i:
        board_tmp[j[0]][j[1]]=1
    visit=[[0]*m for _ in range(n)]
    res=BFS()

    result=max(result, res)
print(result)