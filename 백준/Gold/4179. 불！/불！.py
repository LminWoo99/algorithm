import sys
from collections import deque
input=sys.stdin.readline
def BFS(x,y,fire):
    dq=deque()
    dq.append((x,y,1))
    visit[x][y]=1
    while fire:
        a,b,cnt_f=fire.popleft()
        for i in range(4):
            aa,bb=a+dx[i], b+dy[i]
            if 0<=aa<r and 0<=bb<c and not visit_f[aa][bb] and board[aa][bb]!='#':
                visit_f[aa][bb]=cnt_f+1
                fire.append((aa,bb,cnt_f+1))
    while dq:
        x,y,cnt=dq.popleft()
        if x==r-1 or y==c-1 or x==0 or y==0:
            return cnt
        for i in range(4):
            xx,yy=x+dx[i],y+dy[i]
            if 0<=xx<r and 0<=yy<c and not visit[xx][yy] and board[xx][yy]!='#':
                if not visit_f[xx][yy] or visit_f[xx][yy]>cnt+1:
                    visit[xx][yy]=1
                    dq.append((xx,yy,cnt+1))
            
    return "IMPOSSIBLE"
    
dx=[-1,0,1,0]
dy=[0,1,0,-1]
r,c=map(int, input().split())
board=[list(input().rstrip()) for _ in range(r)]
visit=[[0]*c for _ in range(r)]
visit_f=[[0]*c for _ in range(r)]

fire=deque()
for i in range(r):
    for j in range(c):
        if board[i][j]=='J':
            x,y=i,j
        elif board[i][j]=='F':
            fire.append((i,j,1))
            visit_f[i][j]=1
        
res=BFS(x,y,fire)
print(res)
    
