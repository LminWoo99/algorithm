import sys
input=sys.stdin.readline
from collections import deque

def solution(x, y, cnt):
    global cnt_size
    tmp=0
    dq=deque()
    dq.append((x,y, cnt))
    visit[x][y]=1
    eat=0
    while dq:
        if eat==check:
            break
        else:
            x,y,cnt=dq.popleft()
            for i in range(4): 
                xx, yy= x+dx[i], y+dy[i]
                if 0<=xx<n and 0<=yy<n:
                    if visit[xx][yy][cnt+1]==0 and board[xx][yy]==0:
                        visit[xx][yy][cnt+1]=1

                    elif visit[xx][yy][cnt+1]==0 and board[xx][yy]<cnt_size:
                        visit[xx][yy][cnt+1]=1
                        tmp+=1
                        if tmp==cnt_size:
                            eat+=1
                            tmp=0
                    elif visit[xx][yy][cnt+1]==0 and board[xx][yy]==cnt_size:
                        visit[xx][yy][cnt+1]=1
                    
                    dq.append((xx,yy, cnt+1))
    return cnt
                        

                    
                
n=int(input())
dx=[-1,0,1,0]
dy=[0, -1,0 ,-1]
cnt_size=2
board=[list(map(int, input().split())) for _ in range(n)]
visit=[[[0]*n for _ in range(n)] for _ in range(n)]
check=0
for i in range(n):
    for j in range(n):
        if board[i][j]==9:
            x,y =i,j
        elif board[i][j]!=9 and board[i][j]!=0:
            check+=1
            


cnt=solution(i,j,0)
print(cnt)

