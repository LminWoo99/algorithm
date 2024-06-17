import sys
input=sys.stdin.readline
from collections import deque
dx=[-1,0,1,0]
dy=[0,1,0,-1]
def BFS(rx, ry, bx, by):
    visit=[[[[0]*m for _ in range(n)] for _ in range(m)] for _ in range(n)]
    dq=deque()
    dq.append((rx,ry,bx, by, 1))
    visit[rx][ry][bx][by]=1
    while dq:
        rx, ry, bx, by, cnt= dq.popleft()
        if cnt>10:
            break
        for i in range(4):
            distX,distY=dx[i],dy[i]
            rxx,ryy,r_count=check(rx,ry,distX, distY, 0)
            bxx,byy,b_count=check(bx,by,distX, distY, 0)
            if board[bxx][byy]!='O':
                if board[rxx][ryy]=='O':
                    print(cnt)
                    return
                if rxx==bxx and ryy==byy:
                    if r_count>b_count:
                        rxx-=distX
                        ryy-=distY
                    else:
                        bxx-=distX
                        byy-=distY
                if not visit[rxx][ryy][bxx][byy]:
                    visit[rxx][ryy][bxx][byy]=1
                    dq.append((rxx,ryy,bxx,byy,cnt+1))
    print(-1)
def check(x,y, distX, distY,count):
    while board[x+distX][y+distY]!='#' and board[x][y]!='O':
        count+=1
        x+=distX
        y+=distY
    return x,y,count
n,m=map(int, input().split())
board=[list(input().rstrip()) for _ in range(n)]
for i in range(n):
    for j in range(m):
        if board[i][j]=='R':
            rx, ry=i,j
        elif board[i][j]=='B':
            bx, by=i,j
        elif board[i][j]=='O':
            holeX, holeY=i,j
BFS(rx,ry, bx,by)