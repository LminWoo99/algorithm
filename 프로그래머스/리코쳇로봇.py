dx=[-1,0,1,0]
dy=[0,1,0,-1]
from collections import deque
def solution(board):
    answer = 0
    n=len(board)
    m=len(board[0])
    start_x, start_y=0,0
    end_x, end_y=0,0
    for i in range(n):
        for j in range(m):
            if board[i][j]=='R':
                start_x, start_y=i,j
            elif board[i][j]=='G':
                end_x, end_y=i,j
    def BFS(x,y, end_x, end_y):
        visit=[[0]*m for _ in range(n)]
        dq=deque()
        dq.append((x,y,0))
        visit[x][y]=1
        while dq:
            x,y,cnt=dq.popleft()
            if x==end_x and y==end_y:
                return cnt
            for i in range(4):
                xx_1,yy_1=x+dx[i], y+dy[i]
                if 0<=xx_1<n and 0<=yy_1<m:
                    xx, yy=xx_1, yy_1
                    while True:
                        if 0<=xx<n and 0<=yy<m:
                            if (xx+dx[i]==-1 or yy+dy[i]==-1 or xx+dx[i]==n or yy+dy[i]==m) and (board[xx][yy]=='.' or board[xx][yy]=='G'):
                                if visit[xx][yy]==0:
                                    visit[xx][yy]=1
                                    dq.append((xx, yy, cnt+1))
                                    break
                                else:
                                    break
                            elif board[xx][yy]=='D':
                                    if visit[xx-dx[i]][yy-dy[i]]==0:
                                        visit[xx-dx[i]][yy-dy[i]]=1
                                        dq.append((xx-dx[i], yy-dy[i], cnt+1))
                                        break
                                    else:
                                        break
                        else:
                            break
                        xx,yy=xx+dx[i], yy+dy[i]
                            
                        

        return -1
    answer=BFS(start_x, start_y, end_x, end_y)
    return answer
print(solution(["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]))