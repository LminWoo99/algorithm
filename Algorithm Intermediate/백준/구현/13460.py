import sys
input=sys.stdin.readline
from collections import deque
def BFS(x,y, bx, by, res):
    dq=deque()
    global board
    visit[x][y][bx][by]=1
    dq.append((x,y, bx , by, res))
    while dq:
        x,y, bx, by, res=dq.popleft()
        if res>10:
            break
        for i in range(4):
            distX=dx[i]
            distY=dy[i]
            count=0
            xx,yy, r_count=check(x,y, distX, distY, count)
            bxx,byy, b_count=check(bx,by, distX, distY, count)
            if board[bxx][byy]!='O':
                if board[xx][yy]=='O':
                    print(res)
                    return
                if xx==bxx and yy==byy:
                    if r_count>b_count:
                        xx-=distX
                        yy-=distY
                    else:
                        bxx-=distX
                        byy-=distY
                if not visit[xx][yy][bxx][byy]:
                    visit[xx][yy][bxx][byy]=1
                    dq.append((xx,yy, bxx, byy, res+1))
    print(-1)
        
def check(rx,ry,distX, distY, count):
    while board[rx+distX][ry+distY]!='#' and board[rx][ry]!='O':
        rx+=distX
        ry+=distY
        count+=1
    return rx, ry, count

        
        

dx=[-1,0,1,0]
dy=[0,1,0,-1]

n,m =map(int, input().split())
board=[list(input().rstrip()) for _ in range(n)]
visit=[[[[0]*m for _ in range(n)]for _ in range(m)] for _ in range(n)]
for i in range(n):
    for j in range(len(board[i])):
        if board[i][j]=='B':
            bx , by = i, j
        elif board[i][j]=='R':
            rx, ry= i,j
BFS(rx, ry, bx, by, 1)
