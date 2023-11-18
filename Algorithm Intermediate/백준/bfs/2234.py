import sys
input=sys.stdin.readline

from collections import deque

n,m = map(int, input().split())
castle=[list(map(int , input().split())) for _ in range(m)]

visit=[[0]*n for _ in range(m)]

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]


def BFS(x,y):
    dq=deque()
    dq.append((x,y))
    visit[x][y]=1
    room=1
    while dq:
        x,y=dq.popleft()
        binary=1
        for i in range(4):
            xx=x+dx[i]
            yy=y+dy[i]
            if ((castle[x][y] & binary)!=binary):
                if 0<=xx<m and 0<=yy<n and not visit[xx][yy]:
                    room+=1
                    visit[xx][yy]=1
                    dq.append((xx,yy))
            binary=binary*2
    return room

cnt=0
maxCnt=0
delRoom=0

for i in range(m):
    for j in range(n):
        if visit[i][j]== 0:
            cnt+=1
            maxCnt=max(maxCnt, BFS(i,j))
            
for i in range(m):
    for j in range(n):
        num = 1
        while num < 9:
            if num & castle[i][j]:
                visit=[[0]*n for _ in range(m)]
                castle[i][j] -= num
                delRoom=max(delRoom, BFS(i,j))
                castle[i][j] += num
            num *=2
print(cnt)
print(maxCnt)
print(delRoom)