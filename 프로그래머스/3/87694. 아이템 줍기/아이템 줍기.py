from collections import deque
dx=[-1,0,1,0]
dy=[0,1,0,-1]
def solution(rectangle, characterX, characterY, itemX, itemY):
    board = [[0]*102 for _ in range(102)]
    for cur in rectangle:
        for i in range(cur[1]*2, cur[3]*2+1):
            for j in range(cur[0]*2, cur[2]*2+1):
                if (i==cur[1]*2 or i==cur[3]*2 or j==cur[0]*2 or j==cur[2]*2):
                    if board[i][j]==0:
                        board[i][j]=1
                    elif board[i][j]==1:
                        continue
                else:
                    board[i][j]=2
    def BFS():
        dq=deque()
        visit=[[0]*102 for _ in range(102)]
        visit[characterY*2][characterX*2]=1
        dq.append((characterY*2,characterX*2,0))
        while dq:
            y,x,cnt=dq.popleft()
            if y==itemY*2 and x==itemX*2:
                    return cnt
            for i in range(4):
                yy,xx=y+dy[i], x+dx[i]
                if 2<=xx<102 and 2<=yy<102 and not visit[yy][xx] and board[yy][xx]==1:
                    visit[yy][xx]=1
                    dq.append((yy,xx,cnt+1))
    answer=BFS()
    return answer//2