import sys
input=sys.stdin.readline
from collections import deque
dx=[-1,0,1,0]
dy=[0,-1,0,1]

def bfs(x, y):
    visited = [[0]*n for _ in range(n)]
    dq = deque()
    dq.append((x,y))
    cand = []
    visited[x][y] = 1
    while dq:
        i, j = dq.popleft()
        for idx in range(4):
            ii, jj = i + dx[idx] , j + dy[idx]
            if 0<=ii<n and 0 <= jj<n and visited[ii][jj] == 0:
                if aqua[x][y] > aqua[ii][jj] and aqua[ii][jj] != 0:
                    visited[ii][jj] =  visited[i][j] + 1
                    cand.append((visited[ii][jj] - 1, ii, jj))
                elif aqua[x][y] == aqua[ii][jj]:
                    visited[ii][jj] =  visited[i][j] + 1
                    dq.append([ii,jj])
                elif aqua[ii][jj] == 0:
                    visited[ii][jj] =  visited[i][j] + 1
                    dq.append([ii,jj])
    return sorted(cand, key = lambda x: (x[0], x[1], x[2]))

n=int(input())
aqua=[list(map(int, input().split())) for _ in range(n)]
res=0
for i in range(n):
    for j in range(n):
        if aqua[i][j]==9:
            bx,by=i,j
size=[2,0]
while True:
    aqua[bx][by]=size[0]
    cand=deque(bfs(bx,by))
    if not cand:
        break
    step,xx,yy=cand.popleft()
    res+=step
    size[1]+=1
    if size[0]==size[1]:
        size[0]+=1
        size[1]=0
    aqua[bx][by]=0
    bx,by=xx,yy
print(res)    