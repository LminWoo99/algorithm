import sys
input=sys.stdin.readline
from collections import deque
from itertools import permutations
def solution():
    for x in permutations([0,1,2,3,4]):
        for i in range(5):
            b[x[i]]=board[i]
        DFS(0)
def rotate(b):
    tmp=[[0]*5 for _ in range(5)]
    for i in range(len(b)):
        for j in range(len(b[0])):
            tmp[j][4-i]=b[i][j]
    return tmp
def DFS(L):
    global b
    if L==5:
        if b[4][4][4]:
            BFS(b)
        return
    for i in range(4):
        if b[0][0][0]:
            DFS(L+1)
        b[L]=rotate(b[L])
def BFS(b):
    global result
    dq=deque()
    dist=[[[0,0,0,0,0] for _ in range(5)] for _ in range(5)]
    dq.append((0,0,0))
    while dq:
        h,y,x=dq.popleft()
        if (h,y,x) ==(4,4,4):
            result=min(result, dist[4][4][4])
            if result ==12:
                print(result)
                exit()
            return
        for i in range(6):
            hh=h+dz[i]
            yy=y+dy[i]
            xx=x+dx[i]
            if 0<=hh<5 and 0<=yy<5 and 0<=xx<5 and b[hh][yy][xx]!=0 and dist[hh][yy][xx]==0:
                dq.append((hh,yy,xx))
                dist[hh][yy][xx]=dist[h][y][x]+1
                
    
board=[[list(map(int, input().split())) for _ in range(5)] for _ in range(5)]
b=[[[0]*5 for _ in range(5)] for _ in range(5)]
dx=[-1,0,1,0,0,0]
dy=[0,1,0,-1,0,0]
dz=[0,0,0,0,1,-1]

result=sys.maxsize
solution()
if result==sys.maxsize:
    print(-1)
else:
    print(result)


