import sys
input=sys.stdin.readline
import copy
def move(tmp):
    visit=[[0]*c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if (tmp[i][j]!=-1 and tmp[i][j]!=0):
                for k in range(4):
                    ii ,jj = dx[k]+i, dy[k]+j
                    if 0<=ii<r and 0<=jj<c and tmp[ii][jj]!=-1:
                        board[ii][jj]+=(tmp[i][j]//5)
                        visit[i][j]+=1
                if board[i][j]-(visit[i][j]*(tmp[i][j]//5))<0:
                    board[i][j]=0
                else:
                    board[i][j]-=(visit[i][j]*(tmp[i][j]//5))
def air_up():
    dx=[0,-1,0,1]
    dy=[1,0,-1,0]
    direct, before=0, 0
    x ,y = up,1
    while True:
        nx=x+dx[direct]
        ny=y+dy[direct]
        if x==up and y==0:
            break
        if nx<0 or nx>=r or ny<0 or ny>=c:
            direct+=1
            continue
        board[x][y], before= before, board[x][y]
        x=nx
        y=ny
def air_down():
    dx=[0,1,0,-1]
    dy=[1,0,-1,0]
    direct, before=0, 0
    x ,y = down,1
    while True:
        nx=x+dx[direct]
        ny=y+dy[direct]
        if x==down and y==0:
            break
        if nx<0 or nx>=r or ny<0 or ny>=c:
            direct+=1
            continue
        board[x][y], before= before, board[x][y]
        x=nx
        y=ny    
r,c,t=map(int, input().split())
board=[list(map(int, input().split())) for _ in range(r)]
air_cleaner=[]
dx=[-1,0,1,0]
dy=[0,1,0,-1]
check=[[0]*c for _ in range(r)]
for i in range(r):
    for j in range(c):
        if board[i][j]==-1:
            air_cleaner.append((i,j))
        elif board[i][j]!=0 and board[i][j]!=-1:
            check[i][j]=1
            
time_cnt=0
up = air_cleaner[0][0]
down = air_cleaner[1][0]
while True:
    if time_cnt==t:
        break
    time_cnt+=1
    tmp=copy.deepcopy(board)
    move(tmp)
    air_up()
    air_down()
res=0
for i in range(r):
    for j in range(c):
     if board[i][j]!=-1 and board[i][j]!=0:
         res+=board[i][j]   
print(res)
