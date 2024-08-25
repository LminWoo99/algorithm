from collections import deque
dx=[-1,0,1,0]
dy=[0,1,0,-1]
def BFS(board, f):
    visit=[[0]*len(board[0]) for _ in range(len(board))]
    empty_list=[]
    for i in range(len(board)):
        for j in range(len(board[i])):
            if not visit[i][j] and board[i][j]==f:
                dq=deque()
                dq.append((i,j))
                board[i][j]=1^f
                visit[i][j]=1
                a=[(i,j)]
                while dq:
                    x,y=dq.popleft()
                    for _ in range(4):
                        xx,yy=x+dx[_], y+dy[_]
                        if 0<=xx<len(board) and 0<=yy<len(board[0]) and not visit[xx][yy] and board[xx][yy]==f:
                            dq.append((xx,yy))
                            board[i][j]=1^f
                            visit[xx][yy]=1
                            a.append((xx,yy))
                empty_list.append(a)
    return empty_list
def make(block):
    x,y=zip(*block)
    c,r=max(x)-min(x)+1, max(y)-min(y)+1
    table=[[0]*r for _ in range(c)]
    for i,j in block:
        i,j=i-min(x), j-min(y)
        table[i][j]=1
    return table
def rotate(puzzle):
    rotate=[[0]*len(puzzle) for _ in range(len(puzzle[0]))]
    cnt=0
    for i in range(len(puzzle)):
        for j in range(len(puzzle[i])):
            if puzzle[i][j]==1:
                cnt+=1
            rotate[j][len(puzzle)-i-1]=puzzle[i][j]
    return rotate, cnt
            
def solution(game_board, table):
    answer=0
    empty_blocks=BFS(game_board, 0)
    puzzles=BFS(table, 1)
    
    for empty in empty_blocks:
        filled=False
        table=make(empty)
        for puzzle_origins in puzzles:
            if filled==True:
                break
            puzzle=make(puzzle_origins)
            for i in range(4):
                puzzle,cnt=rotate(puzzle)
                if table==puzzle:
                    answer+=cnt
                    puzzles.remove(puzzle_origins)
                    filled=True
                    break
    return answer