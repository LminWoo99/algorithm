from collections import deque
dx=[-1,0,1,0]
dy=[0,1,0,-1]
def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    board=[[0]*102 for _ in range(102)]
    for r in rectangle:
        x1, y1, x2, y2 = map(lambda x: x*2, r)
        for j in range(y1, y2+1):
            for i in range(x1, x2+1):
                if j==y1 or j==y2:
                    if board[j][i]!=2:
                        board[j][i]=1
                    else:
                        board[j][i]=2
                elif i==x1 or i==x2:
                    if board[j][i]!=2:
                        board[j][i]=1
                    else:
                        board[j][i]=2
                else:
                    board[j][i]=2
    def BFS(x, y):
        dq=deque()
        visit=[[0]*102 for _ in range(102)]
        dq.append((x,y, 0))
        visit[x][y]=1
        while dq:
            x,y,cnt=dq.popleft()
            if x==itemY*2 and y==itemX*2:
                return cnt
            for i in range(4):
                xx, yy=x+dx[i], y+dy[i]
                if 2<=xx<102 and 2<=yy<102 and board[xx][yy]==1 and not visit[xx][yy]:
                    visit[xx][yy]=1
                    dq.append((xx,yy, cnt+1))
    answer=BFS(characterY*2,characterX*2)
        
        
                    
                
    return answer//2

print(solution([[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]], 1, 3, 7, 8))