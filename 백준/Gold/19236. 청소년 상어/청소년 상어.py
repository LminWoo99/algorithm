import sys, copy
input=sys.stdin.readline

board = [[] for _ in range(4)]

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

for i in range(4):
    data = list(map(int, input().split()))
    fish = []
    for j in range(4):
        # 물고기 번호, 방향
        fish.append([data[2*j], data[2*j+1]-1])
    board[i] = fish
max_res=0

def DFS(sx,sy,res, board):
    global max_res
    res+=board[sx][sy][0]
    max_res=max(max_res, res)
    board[sx][sy][0]=0
    for f in range(1, 17):
        f_x, f_y = -1, -1
        for i in range(4):
            for j in range(4):
                if board[i][j][0]==f:
                    f_x, f_y= i,j
                    break
        if f_x ==-1 and f_y==-1:
            continue
        f_d=board[f_x][f_y][1]
        for a in range(8):
            nd= (f_d+a)%8
            nx=f_x+dx[nd]
            ny=f_y+dy[nd]
            if not (0<=nx<4 and 0<=ny<4) or (nx==sx and ny==sy):
                continue
            board[f_x][f_y][1]=nd
            board[f_x][f_y], board[nx][ny]= board[nx][ny], board[f_x][f_y]
            break
            
    s_d=board[sx][sy][1]
    for i in range(1, 5):
        nx=sx+dx[s_d]*i
        ny=sy+dy[s_d]*i
        if 0<=nx<4 and 0<=ny<4 and board[nx][ny][0]>0:
            DFS(nx,ny, res, copy.deepcopy(board))
DFS(0,0,0,board)
print(max_res)
            
    
            