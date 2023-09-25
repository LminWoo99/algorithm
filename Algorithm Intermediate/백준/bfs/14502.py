import sys
input=sys.stdin.readline
from collections import deque
import copy
def BFS():
    dq=deque()
    test=copy.deepcopy(a)
    for i in range(n):
        for j in range(m):
            if a[i][j]==2:
                dq.append((i,j))
    while dq:
        x,y=dq.popleft()
        for i in range(4):
            xx=dx[i]+x
            yy=dy[i]+y
            if 0<=xx<n and 0<=yy<m and test[xx][yy]==0:
                test[xx][yy]=2
                dq.append((xx,yy))
    global result
    count=0
    for i in range(n):
        for j in range(m):
            if test[i][j]==0:
                count+=1
    result=max(result, count)

n,m=map(int, input().split())
a=[list(map(int, input().split())) for _ in range(n)]
dx=[-1,0,1,0]
dy=[0, 1, 0, -1]
result=0
def make_wall(count):
    if count==3:
        BFS()
        return
    for i in range(n):
        for j in range(m):
            if a[i][j]==0:
                a[i][j]=1
                make_wall(count+1)
                a[i][j]=0
                
make_wall(0)
print(result)